function reviewFood() {
    // Replace 'food_content_type_id' and 'food_pk' with the actual content type ID and object ID of the food item
    var content_type_id = '{{ food_content_type_id }}';
    var object_id = '{{ food.pk }}';
    var review_url = `/review/${content_type_id}/${object_id}/`;
    window.location.href = review_url;
}