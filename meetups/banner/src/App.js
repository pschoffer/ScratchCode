import logo from './simplycruit.png';
import './App.css';
import background from './background.jpg'
import gitlab from './gitlab.png'
import qr from './qr.png'

function App() {
  return (
    <div className="background" style={{ backgroundImage: `url(${background})` }}>
      <div className="backdrop">
       <h3>Meetup Group</h3>
       <h2>Norrköping Software Development</h2>
{/*
        <div className="border">
          <h1>Fyne</h1>
          <p>Graphic User Interface Library</p>
        </div>  */}

        <img src={qr}/>
      </div>
    </div>
  );
}

export default App;
