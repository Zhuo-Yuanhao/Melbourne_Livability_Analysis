function (doc) {
  if (doc.place) {
    placeDic = doc.place;
    placeName = placeDic.name;
    box=doc.box
    if (doc.lang=='en'||doc.lang=='en-gb'){
      emit([placeName,'English',box],1);
    }
    else{
      emit([placeName,'NoneEnglish',box],1);
    }
  }
}