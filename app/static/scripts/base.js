// Delete flashed messages 
function deleteSelf(button) {
    button.remove();
}


// Fetch list of blogpost titles for right box
fetch('/api/blogposts/blogpostlist')
    .then(response => response.json())
    .then(function(blogposts) {
        for (let i=0; i<blogposts.length; i++) {
            let item = document.createElement('li');
            let link = document.createElement('a');
            let titles = document.createTextNode(blogposts[i][0]);
            link.appendChild(titles);
            link.href = "/blog/blogposts/" + blogposts[i][1];
            item.appendChild(link);
            document.getElementById("blogposts").appendChild(item);
        }
    });