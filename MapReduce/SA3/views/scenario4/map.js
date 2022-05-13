function (doc) {
  if (doc.place) {
    placeDic = doc.place;
    placeName = placeDic.name;
    if (placeName=='Adelaide'||placeName=='Brisbane'||placeName=='Melbourne'||placeName=='Sydney'){
      emit([placeName],doc.meaningfulLen);
    }
  }
}