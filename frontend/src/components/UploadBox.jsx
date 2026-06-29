import { useRef, useState } from "react";
import api from "../services/api";


function UploadBox({ onPredict,recognized,onImageSelect }) {

    const inputRef = useRef();

    const [image, setImage] = useState(null);

    const [preview, setPreview] = useState(null);

    const [loading, setLoading] = useState(false);


    const chooseImage = (e) => {

        const file = e.target.files[0];

        if (!file) return;

        // Clear previous prediction
        onPredict(null);

        // Update image
        setImage(file);

        setPreview(URL.createObjectURL(file));

        onImageSelect(URL.createObjectURL(file));

    };

    const chooseAnotherImage = () => {

        inputRef.current.click();

    };


    const recognize = async (selectedImage = image) => {

        if (!selectedImage) return;

        setLoading(true);

        console.log("selectedImage:", selectedImage);
        console.log("image state:", image);

        const formData = new FormData();

        console.log("FormData file:", formData.get("file"));

        formData.append("file", selectedImage);

        try{

            const response = await api.post(
                "/predict",
                formData
            );

            onPredict(response.data);

        }

        catch(err){

            console.log(err);

            onPredict({

                success:false,

                message:"Prediction failed."

            });

        }

        setLoading(false);
    };

    return(

        <>

        <div
        className="upload-box"
        onClick={() => inputRef.current.click()}
        >

            {

                preview ?

                <img
                    src={preview}
                    className={
                        recognized
                            ? "preview preview-small"
                            : "preview"
                    }

                    onClick={(e) => {

                        e.stopPropagation();

                        inputRef.current.click();

                    }}
                />

                :

                <>
                    <div className="upload-icon">
                        📸
                    </div>

                    <h3>Drag & Drop an Image</h3>

                    <p>or click to browse</p>

                    <span>PNG • JPG • JPEG</span>
                </>

            }

            <input
                hidden
                ref={inputRef}
                type="file"
                accept="image/*"
                onChange={chooseImage}
                key={preview}
            />

        </div>

        <>
            {
                image && (
                    <button
                        className="upload-btn"
                        onClick={() => recognize()}
                        
                    >

                        {

                            loading

                            ? "Recognizing..."

                            : "Recognize Actor"

                        }

                    </button>
                    
                )
            }
            {
                recognized && (

                    <button
                        className="retry-btn"
                        onClick={chooseAnotherImage}
                    >

                        🔄 Choose Another Image

                    </button>

                )
            }



        </>
    </>
    );

}

export default UploadBox;