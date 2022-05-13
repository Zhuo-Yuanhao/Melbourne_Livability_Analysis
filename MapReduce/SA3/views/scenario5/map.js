function (doc) {
  if (doc.place) {
    placeDic = doc.place;
    placeName = placeDic.name;
    if (placeName=='Adelaide'||placeName=='Brisbane'||placeName=='Melbourne'||placeName=='Sydney'){
      if (doc.infrastructureFlag){
        if (doc.weightedEmotion>0.1){
          emit([placeName,'positive'],1)
        }
        else if(doc.weightedEmotion<-0.1){
          emit([placeName,'negative'],1)
        }
        else{
          emit([placeName,'neutral'],1)
        }
      }
    }
  }
}