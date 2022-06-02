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
    <div className="search">
      <img src={logo} alt="search" />
      <form action="/results" method="get">
        <div className="search__input">
          <input name="q" id="company" type="text" placeholder="Enter a company name." />
        </div>
        <div className="search__buttons">
          <button type="submit">Search</button>
          <label class="switch">
            <input type="checkbox"/>
              <span class="slider round"></span>
          </label>
        </div>
      </form>
    </div>
  )
}

export default Home