function (doc) {
  if (doc.place) {
    placeDic = doc.place;
    placeName = placeDic.name;
    if (placeName=='Adelaide'||placeName=='Brisbane'||placeName=='Melbourne'||placeName=='Sydney'){
      if (doc.num_at<0.5 && doc.num_hash<0.5){
        emit([placeName,'Active'],1);
      }
      else{
        emit([placeName,'NotActive'],1);
      }
    }
  }
}