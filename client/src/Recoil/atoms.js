import {atom} from 'recoil';

export const firstAtom = atom({
        key: 'uniqueKey',
        default: "This is my global variable"
    })

// export const songsToChooseFromAtom = atom({
//     key: 'songsToChooseFrom',
//     default: []
// });