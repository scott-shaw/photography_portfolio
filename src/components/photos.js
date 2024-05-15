import React, {useCallback} from "react";
import 'bootstrap/dist/css/bootstrap.css';
import Gallery from "react-photo-gallery";
import { photos, thumbs } from "../photo_data";
import "../style/photos.css";
import Carousel, { Modal, ModalGateway } from "react-images";

class Photos extends React.Component {
  constructor() {
    super();
      this.state = {
          currentImage: 0,
          viewerIsOpen: false,
      };
  }

  openLightbox = (event, { photo, index }) => {
    this.setState({currentImage: index, viewerIsOpen: true})
  }

  closeLightbox = () => {
    this.setState({currentImage: 0, viewerIsOpen: false})
  }

  componentDidMount() {
    document.title = "Scott Shaw Photography"
  }

  render() {
    return (
      <body>
        <div>
          <Gallery photos={thumbs} direction={"column"} onClick={this.openLightbox} />
          <ModalGateway>
            {this.state.viewerIsOpen ? (
              <Modal onClose={this.closeLightbox}>
                <Carousel
                  currentIndex={this.state.currentImage}
                  views={photos.map(x => ({
                    ...x,
                    srcset: x.srcSet,
                    caption: x.title
                  }))}
                />
              </Modal>
            ) : null}
          </ModalGateway>
        </div>      
      </body>
      
    );
  }
}

export default Photos;
