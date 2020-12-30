StudentBlog Project
======
Resourses:

 - Project based on the directions from second edition of my O'Reilly book [Flask Web Development](http://www.flaskbook.com) with Python, Flask and MySQL

Credits: 

- FAVICON generator: https://favicon.io/
- UNSPLASH <span>Photo by <a href="https://unsplash.com/@jeswinthomas?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Jeswin Thomas</a> on <a href="https://unsplash.com/s/photos/students?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>

<span>Photo by <a href="https://unsplash.com/@kiyun911?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Kiyun Lee</a> on <a href="https://unsplash.com/s/photos/students-computer?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>

<span>Photo by <a href="https://unsplash.com/@element5digital?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Element5 Digital</a> on <a href="https://unsplash.com/s/photos/blog?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
Content: 

- User role implementation presented is a hybrid between discrete roles and permissions.
- Profile Page of the User, where a summary of the user’s participation in the website is presented.
- User-Level Profile Editor and Administrator-Level Profile Editor in two different forms
- Administrator-Level Profile: allows administrators to edit a user’s email, username, confirmed status, and role.
- User Avatar: user avatars provided by Gravatar, the leading avatar service.

- BLOG POSTS: Main features: allow users to read and write blog posts. The form that will be shown in the main page of the application lets users write a blog post. 
    - A blog post is is represented by a title, body, a timestamp, and a one-to-many relationship from the User model. The body field is defined with type db.Text so that there is no limitation on the length.
    - The current user’s permission to write articles is checked before allowing the new post.
    - The user profile page is improved by showing a list of blog posts authored by the user
    - an underscore prefix in the _posts.html: is merely a convention to distinguish standalone and partial templates.
    - to increase the quality of the user experience is used pagination of the data and rendering it in chunks. creating _macros.html template. Macros provide a way to modularize code; they work like functions.
    - pagination template as macros.html
     <!-- Faker package used for generating fake information, creating Fake Blog Post Data -->
    - requirements folder include: dev.txt file can list the dependencies that are necessary for development and a prod.txt file can list the dependencies that are needed in production
    - permament Links to Blog Posts - for sharing link to specific blog post with friends on social networks / (each post will be assigned a page with a unique URL that references it). The URLs that will be assigned to blog posts are constructed with the unique id field assigned when the post is inserted in the database.
    - a post editor that allows users to edit their own posts

- FOLLOWERS: socially aware web application involves keeping track of directional   
links between pairs of users and using these links in database queries. Users are able to “follow” other users and choose to filter the blog post list on the home page to include only those from the users they follow.
 - on home page - to view blog posts from only the users they follow - added with join operation on the home page
 - Cookies can be set only on a response object, so these routes need to create a response object through make_response() instead of letting Flask do this.

- BLOG COMMENTS: 
- comments are displayed on the individual blog post pages that were added as permanent links
- the web form that will be used to enter comments— an simple form that only has a text field and a submit button.
- view function instantiates the comment form and sends it to the post.html tem‐ plate for rendering. The logic that inserts a new comment when the form is submitted is similar to the handling of blog posts
- the link to the comments page is built as the permanent link for the post with a #comments suffix added. This last part is called a URL fragment and is used to indicate an initial scroll position for the page. 
- Permission.MODERATE gives users, who have it in their roles the power to moderate comments made by others. This feature will be exposed as a link in the navigation bar that appears only to users who are permitted to use it. 
    Moderators will see both the notice and the comment body. Moderators will also see a button to toggle the disabled state below each comment. The button invokes one of two new routes, depending on which of the two possible states the comment is changing to.
    The comment enable and disable routes load the comment object, set the disabled field to the proper value, and write it back to the database

Improvements: 
1. Making all users self-followers, it makes the application more usable.
    Creating functions that introduce updates to the database is a common technique used to update applications that are deployed, as running a scripted update is less error than updating databases manually (-> 12e)


