import { Link } from 'react-router-dom';
import "../style/navbar.css";
            /*
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
	                <Link class="nav-item nav-link" to={"/"}>Portfolio</Link>
                </li>
                <li class="nav-item">
	                <Link class="nav-item nav-link" to={"/profile"}>About</Link>
                </li>
            </ul>
            */
function Navbar() {
    return (
      <nav class="navbar navbar-expand-md navbar-dark bg-black">
        <div class="navbar-collapse collapse">
            <ul class="navbar-nav mr-auto">
              <li class="nav-item">
	            <Link class="nav-item nav-link title" to={"/"}>Scott Shaw Photography</Link>
              </li>
            </ul>
        </div>
    </nav>
    );
}

export default Navbar;

