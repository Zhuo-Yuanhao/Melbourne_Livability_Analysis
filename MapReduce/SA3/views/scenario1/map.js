function (doc) {
  if (doc.place) {
    placeDic = doc.place;
    placeName = placeDic.name;
    if (placeName=='Adelaide'||placeName=='Brisbane'||placeName=='Melbourne'||placeName=='Sydney'){
      if (doc.lang=='en'||doc.lang=='en-gb'){
        emit([placeName,'English'],1);
      }
      else{
        emit([placeName,'NoneEnglish'],1);
      }
    }
  }
}