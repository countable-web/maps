import { getCookie, getApiUrl } from '@/plugins/utils.js'

export const state = () => ({
  user: null,
  picture: null,
  isLoggedIn: false,
  notifications: null,
  mediaToVerify: null,
  placesToVerify: null,
  membersToVerify: null
})

export const mutations = {
  setUser(state, user) {
    state.user = Object.assign({}, user)
  },

  setPicture(state, pic) {
    state.picture = pic
  },

  setLoggedIn(state, loggedIn) {
    state.isLoggedIn = loggedIn
  },

  setNotification(state, notifications) {
    state.notifications = notifications
  },
  setMediaToVerify(state, mtv) {
    state.mediaToVerify = mtv
  },
  setPlacesToVerify(state, ptv) {
    state.placesToVerify = ptv
  },
  setMembersToVerify(state, utv) {
    state.membersToVerify = utv
  }
}

export const actions = {
  async favorite({ commit }, data) {},
  async saveLocation({ commit }, data) {
    const headers = {
      headers: {
        'X-CSRFToken': getCookie('csrftoken')
      }
    }
    try {
      const result = await this.$axios.post(`/api/favourite/`, data, headers)
      return result
    } catch (e) {
      return { error: e, status: 'failed' }
    }
  },

  async approve({ commit }, data) {
    const headers = {
      headers: {
        'X-CSRFToken': getCookie('csrftoken')
      }
    }
    const mode = data.verify ? 'verify' : 'reject'
    const result = await this.$axios.patch(
      `${getApiUrl(`${data.type}/${data.tv.id}/${mode}/`)}`,
      {
        status_reason: mode
      },
      headers
    )
    return result
  },

  async addNotification({ commit }, data) {
    const headers = {
      headers: {
        'X-CSRFToken': getCookie('csrftoken')
      }
    }
    const result = await this.$axios.post(
      getApiUrl(`notification/`),
      data,
      headers
    )
    return result
  },

  async getNotifications({ commit }, data) {
    let result = null
    if (data.isServer) {
      result = await this.$axios.get(
        getApiUrl(`notification?timestamp=${new Date().getTime()}/`)
      )
    } else {
      const headers = {
        headers: {
          'X-CSRFToken': getCookie('csrftoken')
        }
      }
      result = await this.$axios.get(
        getApiUrl(`notification?timestamp=${new Date().getTime()}/`),
        {},
        headers
      )
    }

    commit('setNotification', result.data)
    return result
  },

  async deleteMedia({ commit, dispatch }, data) {
    const headers = {
      headers: {
        'X-CSRFToken': getCookie('csrftoken')
      }
    }
    const result = await this.$axios.delete(
      getApiUrl(`media/${data.id}/`),
      headers
    )
    if (data.type === 'placename') {
      await dispatch(
        'places/getPlaceMedias',
        {
          id: data.type_id
        },
        { root: true }
      )
      await dispatch('user/getMediaToVerify', {}, { root: true })
    }

    if (data.type === 'community') {
      await dispatch(
        'places/getPlaceMedias',
        {
          id: data.type_id
        },
        { root: true }
      )
      await dispatch('user/getMediaToVerify', {}, { root: true })
    }

    return result
  },

  async getPlacesToVerify({ commit }, data) {
    const result = await this.$axios.$get(
      `${getApiUrl(
        `placename/list_to_verify?timestamp=${new Date().getTime()}/`
      )}`
    )
    commit('setPlacesToVerify', result)
    return result
  },

  async getMediaToVerify({ commit }, data) {
    const result = await this.$axios.$get(
      `${getApiUrl(`media/list_to_verify?timestamp=${new Date().getTime()}/`)}`
    )
    commit('setMediaToVerify', result)
    return result
  },

  async getMembersToVerify({ commit }, data) {
    const result = await this.$axios.$get(
      `${getApiUrl(
        `community/list_member_to_verify?timestamp=${new Date().getTime()}/`
      )}`
    )
    commit('setMembersToVerify', result)
    return result
  },

  async setLoggedInUser({ commit }, data) {
    const result = await this.$axios.$get(
      `${getApiUrl(`user/auth?timestamp=${new Date().getTime()}/`)}`
    )
    console.log('Dispatch Result', result)
    commit('setUser', result.user)
    commit('setPicture', result.user.picture)
    return result
  },

  async flagContent({ commit, dispatch }, data) {
    const headers = {
      headers: {
        'X-CSRFToken': getCookie('csrftoken')
      }
    }

    const result = await this.$axios.$patch(
      `${getApiUrl(`${data.type}/${data.id}/flag/`)}`,
      {
        status_reason: data.reason
      },
      headers
    )

    if (data.type === 'placename') {
      await dispatch(
        'places/getPlace',
        {
          id: data.id
        },
        { root: true }
      )
    } else if (data.type === 'media') {
      await dispatch(
        'places/getPlaceMedias',
        {
          id: data.belongid
        },
        { root: true }
      )
    }
    return result
  }
}
