function ActorSelector({

    actors,

    selectedActor,

    setSelectedActor

}) {

    return (

        <div className="actor-selector">

            {

                actors.map((actor,index)=>(

                    <button

                        key={index}

                        className={
                            selectedActor===index
                                ? "actor-pill active"
                                : "actor-pill"
                        }

                        onClick={()=>setSelectedActor(index)}

                    >

                        🎭 {actor.actor}

                    </button>

                ))

            }

        </div>

    );

}

export default ActorSelector;