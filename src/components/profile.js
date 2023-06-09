import React from "react";
import 'bootstrap/dist/css/bootstrap.css';
import "../style/profile.css";

class Profile extends React.Component {
  constructor() {
    super();
      this.state = {};
  }

  componentDidMount() {
    document.title = "Scott Shaw Photography"
  }

  render() {
    return (
      <body>
      </body>
    );
  }
}

export default Profile;
