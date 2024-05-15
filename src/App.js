import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import Photos from "./components/photos";
import Navbar from "./components/navbar"
import Profile from "./components/profile";
import Locations from "./components/locations";

function App() {
    return (
      <Router>
        <Navbar/>
        <Routes>
          <Route path="/" element={<Photos/>}/>
          <Route path="/profile" element={<Profile/>}/>
          <Route path="/locations" element={<Locations/>}/>
        </Routes>
      </Router>  
    );
}

export default App;
