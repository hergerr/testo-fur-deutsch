import React from "react";
import "./learning-set-box.styles.css";

export const LearningSetBox = (props) => (
    <div className="LearningSetBox-container">
        <p className="LearningSetBox-title-and-date">{props.title_and_date}</p>
        <p className="LearningSetBox-progress">{props.progress}</p>
    </div>
)