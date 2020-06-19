import React from 'react'
import './word-quiz-page.styles.css'

import { WordBox } from '../../components/word-box/word-box.component'

export const WordQuizPage = () => (
    <div className="WordQuizPage-container">
        <h3>Arbeiten</h3>

        <div className="WordQuizPage-word-wrapper">
            <div className="WordQuizPage-column">
                <div className="WordQuizPage-word-option">
                    <WordBox word="pracować" />
                </div>
                <div className="WordQuizPage-word-option">
                    <WordBox word="robić" />
                </div>
            </div>
            <div className="WordQuizPage-column">
                <div className="WordQuizPage-word-option">
                    <WordBox word="czesać" />
                </div>
                <div className="WordQuizPage-word-option">
                    <WordBox word="prać" />
                </div>
            </div>
        </div>
    </div>
)