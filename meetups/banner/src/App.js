import bnb from './bnb.svg';
import eth from './eth.svg';
import btc from './btc.svg';
import avax from './avax.svg';
import './App.css';
import background from './background.jpg'

function App() {
  return (
    <div className="background" style={{ backgroundImage: `url(${background})` }}>
      <div className="backdrop">
        <h2>How Is It Built:</h2>
        <div className='border' >
          <h2 style={{color: 'black'}}>Blockchain(s)</h2>
          <div style={{ flexDirection: 'row' }}>
            <img className="logo" src={eth} />
            <img className="logo" src={btc} />
            <img className="logo" src={avax} />
            <img className="logo" src={bnb} />
          </div>
        </div>


      </div>
    </div>
  );
}

export default App;
