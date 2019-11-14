for i in *.mp4;
  do name=`echo "$i" | cut -d'.' -f1`
  if [ ! -d "/home/nudlesoup/Research/MakingImagesfromDataset/EgoCentricImages/$name" ]; then
   mkdir -p "/home/nudlesoup/Research/MakingImagesfromDataset/EgoCentricImages/$name"
   ffmpeg -i "$i" -vf fps=0.5 "/home/nudlesoup/Research/MakingImagesfromDataset/EgoCentricImages/$name/$name%03d.jpg"
  fi
done
