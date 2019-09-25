// TODO: define addFavoriteBook(..) function
var favoriteBooks = [];

function addFavoriteBook(bookName){

    if(bookName.includes('Great') == false){
        favoriteBooks.push(bookName);
    }

}


// TODO: define printFavoriteBooks() function
function printFavoriteBooks(){
    console.log(`Favorite books: ${favoriteBooks.length}`)
    for(let books of favoriteBooks){
        console.log(books);
    }

}

addFavoriteBook("A Song of Ice and Fire");
addFavoriteBook("The Great Gatsby");
addFavoriteBook("Crime & Punishment");
addFavoriteBook("Great Expectations");
addFavoriteBook("You Don't Know JS");
printFavoriteBooks();
// TODO: print out favorite books
