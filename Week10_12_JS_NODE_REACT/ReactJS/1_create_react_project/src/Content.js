import ItemList from './ItemList'
/*
const Content = () => {

  // useState Hook 
  // Syntax  : const [getter , setter] = useState(initial_getter)
  const [name , setName] = useState('Ajay')
  const [count , setCount] = useState(0)

  const handleNameChange = () => {
    const names = ['Ajay' , 'Eniyan' , 'Anirudh'];
    const int = Math.floor(Math.random() * 3);
    setName(names[int]);

  }

  const CountClick1 = () => {
    setCount(count + 1)
    setCount(count + 1)
    console.log(count)
  }

  const CountClick2 = () => {
    console.log(count)
  }



  // click events
  const handleDoubleClick = () => {
    console.log("you double clicked it")
  }

  const handleClick1 = (name) => {
    console.log(`${name} was clicked`)
  }  
  
  const handleClick2 = (e) => {
    console.log(e.target.innerText)
  }



    return (
        <main>
            <p onDoubleClick={handleDoubleClick}>
                Hello {name}!
            </p>

            <button onClick ={handleNameChange}>Change name</button>
            <button onClick ={() => handleClick1('Ajay')}>Click It</button>
            <button onClick ={(e) => handleClick2(e)}>Click It</button>


            <button onClick ={CountClick1}>Count click 1</button>
            <button onClick ={CountClick2}>Count click 2</button>
        </main>
    )
}

*/

const Content = ({items , handleCheck , handleDelete}) => {
    return(
      <>
        {items.length ? (
            < ItemList
                items = {items}
                handleCheck = {handleCheck}
                handleDelete = {handleDelete}
            />
        ) : (
          <p style = { {marginTop : '2rem'}}>Your list is empty </p>
        )}
      </>
    )
}

export default Content;

