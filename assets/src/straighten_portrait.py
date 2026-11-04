import cv2, numpy as np, sys
im=cv2.imread("suit_clean.jpg")
H,W=im.shape[:2]
fc=(312.0,438.0)            # face centre (Haar box centre)
def make(angle, out, side=840, off=(148,107), size=1024):
    M=cv2.getRotationMatrix2D(fc, angle, 1.0)
    rot=cv2.warpAffine(im,M,(W,H),flags=cv2.INTER_LANCZOS4,borderMode=cv2.BORDER_CONSTANT)
    valid=cv2.warpAffine(np.full((H,W),255,np.uint8),M,(W,H),flags=cv2.INTER_NEAREST)
    cx,cy=fc[0]+off[0],fc[1]+off[1]
    s=side
    while s>500:
        x0,y0=int(cx-s/2),int(cy-s/2)
        if x0>=0 and y0>=0 and x0+s<=W and y0+s<=H and valid[y0:y0+s,x0:x0+s].min()==255: break
        s-=10
    crop=rot[y0:y0+s,x0:x0+s]
    up=cv2.resize(crop,(size,size),interpolation=cv2.INTER_LANCZOS4)
    blur=cv2.GaussianBlur(up,(0,0),1.0)
    res=cv2.addWeighted(up,1.3,blur,-0.3,0)   # light unsharp mask only: no denoise, no tone change
    cv2.imwrite(out,res,[cv2.IMWRITE_JPEG_QUALITY,95])
    print(out,"angle",angle,"side",s)
make(-9.4,'pp_final.jpg')

