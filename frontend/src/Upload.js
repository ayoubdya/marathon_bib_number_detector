import './Upload.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import {useState,useEffect} from 'react';
import { Modal} from 'react-bootstrap';
import { Link } from 'react-router-dom';


export default function Upload(){
    const [selectedFiles, setSelectedFiles] = useState([]);
    const [showModal, setShowModal] = useState(false);


    const handleFileChange = (e) => {
        const files = Array.from(e.target.files); // Convertit la liste de fichiers en tableau
        const filesWithPreview = files.map(file => ({
            file,
            preview: URL.createObjectURL(file) // Crée une URL temporaire pour chaque fichier
        }));
        setSelectedFiles(filesWithPreview); // Met à jour l'état avec les fichiers et leurs URLs de prévisualisation
        setShowModal(true); // Afficher la modal après l'upload des fichiers
    };
    useEffect(() => {
        // Cleanup URLs on component unmount
        return () => {
            selectedFiles.forEach(fileObj => URL.revokeObjectURL(fileObj.preview));
        };
    }, [selectedFiles]);

    return( 
     <div className=" Upl container-fluid d-flex justify-content-center align-items-start flex-column ">
     <div className='col-md-6'>
      <h1 className="text-left text-white " style={{ paddingLeft: '10px' }}>Upload Your Marathon Photos</h1>
      <p className="text-left  text-white" style={{ paddingLeft: '10px', width:'75%',fontWeight:'bold' }}>
        Easily upload your marathon photos here. Select your photos from your device and click 'Upload' to store them securely. Our system will automatically organize them based on the bib numbers of the participants.
      </p>
      <div className="d-flex justify-content-center">
      <label className="custom-file-upload">
    <input type="file" multiple className="form-control-file text-white" onChange={handleFileChange} />
     <span>Upload</span>
   </label>
    </div>
    </div>
    <Modal style={{paddingTop:'74px'}} show={showModal} onHide={() => setShowModal(false)}>
                <Modal.Header closeButton>
                    <Modal.Title>Uploaded Images</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <div className="preview-container">
                        {selectedFiles.map((fileObj, index) => (
                            <img key={index} src={fileObj.preview} alt={fileObj.file.name} width="100" style={{ margin: '5px' }} />
                        ))}
                    </div>
                </Modal.Body>
                <Modal.Footer >
                    <Link className='btn2' onClick={() => setShowModal(false)}>
                        <span>Close</span>
                    </Link>
                </Modal.Footer>
            </Modal>
    </div>
    
    );
}