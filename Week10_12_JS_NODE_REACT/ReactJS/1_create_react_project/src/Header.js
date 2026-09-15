

// Default props(properties)
const Header = ({title = "Default Title"}) => {

    return (
        <header>
            <h1>{title}</h1>
        </header>
    )
}


export default Header;



// inline css

// const Header = () => {

//     const headerStyle = {
//         backgroundColor : 'royalblue',
//         color : '#fff'
//     };

//     return (
//         <header style = {headerStyle}>
//             <h1> Groceries List</h1>
//         </header>
//     )
// }
