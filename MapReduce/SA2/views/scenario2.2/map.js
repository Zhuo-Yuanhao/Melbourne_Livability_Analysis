function (doc) {
  if (doc.place) {
    placeDic = doc.place;
    placeName = placeDic.name;
    date = new Date(doc.created_at);
    date.setHours(date.getHours() + 10);
    month = date.getMonth() + 1;
    day = date.getDate();
    box=doc.box
    if (doc.lang=='en'||doc.lang=='en-gb'){
      emit([placeName,box,month,day],doc.weightedEmotion)
    }
  }
}