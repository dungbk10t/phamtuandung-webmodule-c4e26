from ex1 import posts_collection

new_post = {
        "title":"You are the apple of my eyes",
        "author":"Cửu Bá Đao",
        "content":"Tuổi thanh xuân giống như một cơn mưa rào, dù cho bạn từng bị cảm lạnh vì tắm mưa thì bạn vẫn muốn được đắm mình trong cơn mưa ấy lần nữa",
}
new_post1 = {
        "title":"You are the apple of my eyes",
        "author":"Cửu Bá Đao",
        "content":"Tớ rất thích cậu. Cực kì thích cậu. Sẽ có một ngày, tớ sẽ theo đuổi được cậu. Nghìn vạn phần trăm sẽ theo đuổi được cậu. Tớ không hỏi, nên cậu cũng không được từ chối tớ. Hãy để tớ tiếp tục thích cậu đi",
}
new_post2 = {
        "title":"Our times",
        "author":"Trần Ngọc San",
        "content":"Bạn có thích bản thân của hiện tại không? Khi lớn lên, chúng ta sẽ vì cuộc sống mà trở nên khôn ngoan hơn, cũng dễ dàng nhượng bộ thỏa hiệp. Biến thành người mà chính bản thân mình cũng không nhận ra. Có khi nào bạn nhớ bản thân mình của thì quá khứ không? Lúc mà các bạn có hoài bão, dám ước mơ. Cái tôi đó, bạn còn giữ nó không?",
}
posts_collection.insert_one(new_post)
posts_collection.insert_one(new_post1)
posts_collection.insert_one(new_post2)

