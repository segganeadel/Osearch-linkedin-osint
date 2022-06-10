import logo from "../../images/magnifier.png"
import "./Home.scss"


const Home = () => {

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
        </form>
      </div>
    </div>
  )
}

export default Home