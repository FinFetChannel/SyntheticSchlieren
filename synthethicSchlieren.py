import cv2

cap = cv2.VideoCapture('sample.mp4')
##cap.set(cv2.CAP_PROP_POS_FRAMES, 80) # skip to a specific frame
ret, img = cap.read()
background = img

count = 1
meanframe = cv2.absdiff(img, background)

frameh, framew, ch = img.shape
writer = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('out.avi',  writer, 30, (framew,frameh))


while(ret):

    frame = cv2.absdiff(img, background)

    ret,frame = cv2.threshold(frame,20,255,cv2.THRESH_TOZERO) # adjust the 20
    ret,frame = cv2.threshold(frame,60,255,cv2.THRESH_TOZERO_INV) # adjust the 60
    frame = frame*4
    
    meanframe = cv2.addWeighted(meanframe, 1-1/count, frame, 1/count,  0)
    count = count+1
    frame = cv2.absdiff(frame, meanframe)

##    frame = cv2.blur(frame,(5,5))
##    frame = cv2.GaussianBlur(frame,(5,5),0)
##    frame = cv2.medianBlur(frame,5)

    cv2.imshow('frame', frame)
    out.write(frame)
##    background = img # Use only when background is moving
    ret, img = cap.read()

    k = cv2.waitKey(33)
    if k==27:    # Esc key to stop
        break

cap.release()
out.release()
cv2.destroyAllWindows()
