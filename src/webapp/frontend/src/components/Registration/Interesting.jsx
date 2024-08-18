import React from "react";
import classes from "./Registration.module.scss"
import buttons from "../../sass/Buttons.module.scss"
import interesting from "./Interesting.module.scss"
import { useNavigate } from "react-router-dom";
// Контейнер для содержимого страниц. Ограничивает его ширину.
const Container = ({ children }) => {
    let navigate = useNavigate()
    return <>
        <div className={classes.center}>
            <p className={classes.centered_text}>Кто тебе интересен?</p>
            <div className={interesting.buttonsinteresting}>
                    <div className={interesting.firstrow}>
                        <button className={[buttons.btn, interesting.btn].join(" ")}>Девушки</button>
                        <button className={[buttons.btn, interesting.btn].join(" ")}>Парни</button>
                    </div>
                    <div className={interesting.secondrow}>
                        <button className={[buttons.btn, interesting.btn].join(" ")}>Все равно</button>
                    </div>
				</div>
        </div>
        <div className={classes.bottom}>
            <div className={classes.bottom_nav}>
                <button className={[buttons.btn, classes.btn].join(" ")} onClick={() => { navigate("/register/birthday") }}>Давай начнем</button>
            </div>
        </div>
    </>;
};

export default Container;