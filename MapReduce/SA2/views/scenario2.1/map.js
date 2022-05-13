function (doc) {
  if (doc.place) {
    placeDic = doc.place;
    placeName = placeDic.name;
    box=doc.box
    if (doc.lang=='en'||doc.lang=='en-gb'){
      if (doc.weightedEmotion>0.1){
        emit([placeName,'positive',box],1)
      }
      else if(doc.weightedEmotion<-0.1){
        emit([placeName,'negative',box],1)
      }
      else{
        emit([placeName,'neutral',box],1)
      }
    }
  }
}