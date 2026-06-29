import { useState, useEffect } from "react";

import UploadBox from "../components/UploadBox";
import ActorCard from "../components/ActorCard";
import MovieGrid from "../components/MovieGrid";
import ActorSelector from "../components/ActorSelector";



function Home() {

    const [prediction, setPrediction] = useState(null);
    const [selectedActor,setSelectedActor]=useState(0);
    const [uploadedImage, setUploadedImage] = useState(null);
    const [recognized, setRecognized] = useState(false);
    const [error, setError] = useState(null);


    useEffect(() => {

        if(prediction){

            setTimeout(()=>{

                document
                    .getElementById("movies")
                    ?.scrollIntoView({
                        behavior:"smooth"
                    });

            },600);

        }

    },[prediction]);
    return (

        <div className="home">

            <h1 className="logo">
                🎬 CineVision AI
            </h1>

            <h2 className="title">
                Discover Movies Through Faces
            </h2>

            <p className="subtitle">
                Recognize actors from a single image and instantly
                explore their best movies.
            </p>

            <UploadBox

                recognized={recognized}

                onImageSelect={setUploadedImage}

                onPredict={(data)=>{

                    // Image changed → clear everything
                    if(data===null){

                        setPrediction(null);

                        setRecognized(false);

                        setError(null);

                        return;

                    }

                    if(data.success){

                        setPrediction(data);

                        setRecognized(true);

                        setSelectedActor(0);

                        setError(null);

                    }

                    else{

                        setPrediction(null);

                        setRecognized(false);

                        setError(data.message || "Something went wrong.");

                    }

                }}
            />
            {

                error &&

                <div className="error-card">

                    ❌ {error}

                </div>

            }
            {
                prediction &&

                <h2
                    style={{
                        textAlign: "center",
                        marginTop: "50px"
                    }}
                >
                    {prediction.num_faces} Actor
                    {prediction.num_faces > 1 ? "s" : ""}
                    {" "}Detected
                </h2>
            }


            {
                prediction && (
                    <>

                        <ActorSelector

                            actors={prediction.actors}

                            selectedActor={selectedActor}

                            setSelectedActor={setSelectedActor}

                        />

                        <ActorCard

                            result={prediction.actors[selectedActor]}

                        />

                        <div id="movies">

                            <MovieGrid

                                movies={

                                    prediction.actors[selectedActor].movies

                                }

                            />

                        </div>

                    </>
                    
                    

                )
            }

        </div>

    );

}

export default Home;