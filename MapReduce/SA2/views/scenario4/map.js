function (doc) {
  if (doc.place) {
    placeDic = doc.place;
    placeName = placeDic.name;
    box=doc.box
    emit([placeName,box],doc.meaningfulLen);
  }
}