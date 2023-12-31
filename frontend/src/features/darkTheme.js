import { createSlice } from '@reduxjs/toolkit';

export const initialStateValue = true;

export const darkThemeSlice = createSlice({
  name: 'theme',
  initialState: {
    theme: initialStateValue,
  },
  reducers: {
    setTheme: (state) => {
      state.theme = !state.theme;
    }
  }
});

export const { setTheme } = darkThemeSlice.actions;
export default darkThemeSlice.reducer;