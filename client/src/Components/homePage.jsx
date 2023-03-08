import React from 'react';
import {firstAtom} from '../Recoil/atoms.js';
import { useRecoilState } from 'recoil';

function HomePage() {
    const [globalVariable, setGlobalVariable] = useRecoilState(firstAtom)
    return (
        <div className="HomePage">
            <p>{globalVariable}</p>
        </div>
    );
}

export default HomePage;