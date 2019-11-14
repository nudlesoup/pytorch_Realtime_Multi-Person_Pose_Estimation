for i in *.mp4;
  do name=`echo "$i" | cut -d'.' -f1`
  if [ ! -d "/home/nudlesoup/Research/MakingImagesfromDataset/NonEgoCentricImages/$name" ]; then
   mkdir -p "/home/nudlesoup/Research/MakingImagesfromDataset/NonEgoCentricImages/$name"
   ffmpeg -i "$i" -vf fps=1 "/home/nudlesoup/Research/MakingImagesfromDataset/NonEgoCentricImages/$name/$name%03d.jpg"
  fi
done
