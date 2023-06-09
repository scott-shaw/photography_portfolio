import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import Photos from "./components/photos";
import Navbar from "./components/navbar"
import Profile from "./components/profile";

function App() {
    return (
      <Router>
        <Navbar/>
        <Routes>
          <Route path="/" element={<Photos/>}/>
          <Route path="/profile" element={<Profile/>}/>
        </Routes>
      </Router>  
    );
}

export default App;
