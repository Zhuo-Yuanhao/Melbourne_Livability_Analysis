function (doc) {
  if (doc.place) {
    placeDic = doc.place;
    placeName = placeDic.name;
    if (placeName=='Adelaide'||placeName=='Brisbane'||placeName=='Melbourne'||placeName=='Sydney'){
      date = new Date(doc.created_at);
      date.setHours(date.getHours() + 10);
      month = date.getMonth() + 1;
      day = date.getDate();
      if (doc.lang=='en'||doc.lang=='en-gb'){
        emit([placeName,month,day],doc.weightedEmotion)
      }
    }
  }
}