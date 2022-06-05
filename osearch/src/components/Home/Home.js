import logo from "../../images/magnifier.png"
import "./Home.css"


const Home = () => {
  // const [inputText, setInputText] = useState("");
  // let inputHandler = (e) => {
  //   //convert input text to lower case
  // var lowerCase = e.target.value.toLowerCase();
  // setInputText(lowerCase);
  // console.log(lowerCase);
  // }
  return (
    <div className="flexbox">
      <div className="search">
        <img src={logo} alt="search" />
        <form action="/results" method="get">
          <div className="search__input">
            <input name="q" id="company" type="text" placeholder="Saisir le nom d'une société." />
          </div>
          <div className="search__buttons">
            <button type="submit">Recherche</button>
          </div>
          <div className="flexbox-row">
          <label className="switch">
            <input type="checkbox" name="active" />
            <span className="slider round"></span>
          </label>
          <h3>Recherche active</h3>
          </div>
        </form>
      </div>
    </div>
  )
}

export default Home