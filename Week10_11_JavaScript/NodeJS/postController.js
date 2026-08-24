const posts = [
    {id : 1 , title : 'Post One'},
    {id : 2 , title : 'Post Two'},
];

// -> one method of export 
// export const getPosts= () => posts; 


// -> another method of export 
const getPosts = () => posts;
export {getPosts};