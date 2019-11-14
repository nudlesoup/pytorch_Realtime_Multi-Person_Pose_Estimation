for i in *.mp4;
  do name=`echo "$i" | cut -d'.' -f1`
  echo "$name"
#  path = "/home/nudlesoup/Research/MakingImagesfromDataset/NonEgoCentricImages/$name"
  mkdir -p "/home/nudlesoup/Research/MakingImagesfromDataset/NonEgoCentricImages/$name"
done
