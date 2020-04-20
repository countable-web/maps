export const state = () => ({
  isDetailMode: false,
  mobileContent: false, // This should be isMobileContent, since it is boolean
  isArtsMode: false,
  showGallery: false, // This should be isGalleryShown -> not sure how this functions so my naming might be inaccurate. But this shouldn't start with show (action)
  collapseDetail: false, // This should be isSideBarCollapsed
  showLoading: false // isDataLoading
})

export const mutations = {
  set(state, isDetailMode) {
    state.isDetailMode = isDetailMode
  },

  setMobileContent(state, mobileContent) {
    state.mobileContent = mobileContent
  },

  setDrawerContent(state, value) {
    state.isArtsMode = value
  },

  setGallery(state, value) {
    state.showGallery = value
  },
  toggleCollapse(state, value) {
    state.collapseDetail = value
  },
  toggleLoading(state, value) {
    state.showLoading = value
  }
}
