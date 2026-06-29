import { useRef, useState } from "react";

function FaceOverlay({

    image,

    actors,

    selectedActor,

    setSelectedActor

}){

    const imageRef = useRef();

    const [scale, setScale] = useState({

        x:1,

        y:1

    });

    if(!image || !actors) return null;

    return(

        <div className="face-container">

            <img

                ref={imageRef}

                src={image}

                className="face-image"

                onLoad={(e)=>{

                    const img = e.target;

                    setScale({

                        x: img.clientWidth / img.naturalWidth,

                        y: img.clientHeight / img.naturalHeight

                    });

                }}

            />

            {

                actors.map((actor,index)=>{

                    const [

                        x1,

                        y1,

                        x2,

                        y2

                    ] = actor.bbox;

                    return(

                        <div

                            key={index}

                            className={

                                selectedActor===index

                                ?

                                "face-box active"

                                :

                                "face-box"

                            }

                            style={{

                                left:x1*scale.x,

                                top:y1*scale.y,

                                width:(x2-x1)*scale.x,

                                height:(y2-y1)*scale.y

                            }}

                            onClick={()=>setSelectedActor(index)}

                        >

                            <span>

                                {actor.actor}

                            </span>

                        </div>

                    );

                })

            }

        </div>

    );

}

export default FaceOverlay;