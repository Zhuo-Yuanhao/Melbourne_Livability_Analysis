function (doc) {
  if (doc.place) {
    placeDic = doc.place;
    placeName = placeDic.name;
    box=doc.box
    if (doc.num_at<0.5 && doc.num_hash<0.5){
      emit([placeName,'Active',box],1);
    }
    else{
      emit([placeName,'NotActive',box],1);
    }
  }
}