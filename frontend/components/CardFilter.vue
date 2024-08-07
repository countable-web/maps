<template>
  <div class="filter-container">
    <b-form-input
      id="search-artist-input"
      v-model="searchFilter"
      type="search"
      class="search-input"
      :placeholder="filterPlaceholder()"
      autocomplete="off"
      @input="updateQuery"
    >
    </b-form-input>
    <img
      class="search-icon"
      src="@/assets/images/search_icon.svg"
      alt="Search"
    />
  </div>
</template>

<script>
export default {
  props: {
    mode: {
      default: '',
      type: String
    }
  },
  data() {
    return {
      searchFilter: ''
    }
  },
  computed: {
    artQuery() {
      return this.$store.state.arts.artSearch
    },
    grantQuery() {
      return this.$store.state.grants.grantSearch
    },
    searchQuery() {
      return this.mode === 'arts' ? this.artQuery : this.grantQuery
    },
    isDrawerShown() {
      return this.$store.state.sidebar.isArtsMode
    },
    filterMode() {
      return this.$store.state.arts.filter
    },
    isMobileSideBarOpen() {
      return this.$store.state.responsive.isMobileSideBarOpen
    }
  },
  mounted() {
    this.$root.$on('clearInput', () => {
      this.searchFilter = ''
    })

    this.searchFilter = this.mode === 'arts' ? this.artQuery : this.grantQuery
  },
  methods: {
    updateQuery(value) {
      // Check if slider is closed, open when typing
      if (!this.isMobileSideBarOpen) {
        if (value.length !== 0) {
          this.$root.$emit('openSideBarSlider')
        }
      } else if (value.length === 0) {
        this.$root.$emit('closeSideBarSlider')
      }

      if (this.isDrawerShown) {
        this.$store.commit('sidebar/setDrawerContent', false)
      }

      if (this.mode === 'arts') {
        this.$store.commit('arts/setArtSearch', value)
      } else {
        this.$store.commit('grants/setGrantsSearch', value)
      }
    },
    resetValue() {
      this.$store.commit('arts/setArtSearch', '')
      this.$store.commit('grants/setGrantsSearch', '')
    },
    filterPlaceholder() {
      if (this.mode === 'arts') {
        const mode = this.filterMode
        if (mode === 'artwork') {
          return `Search for artist name, or medium...`
        } else {
          return `Search for ${
            mode === 'public_art' ? 'public art' : mode
          }'s name...`
        }
      } else {
        return 'Search for grants name...'
      }
    }
  }
}
</script>

<style>
.filter-container {
  position: relative;
  display: flex;
  width: 90%;
  margin: 1em 1em 0.25em 1em;
}

@media (max-width: 993px) {
  .filter-container {
    width: 95%;
    margin: 0 0 0.25em 0;
  }

  .grants-main-container .filter-container {
    width: 100%;
    margin: 0 0 0 0;
  }
}

.search-input::placeholder {
  color: #707070;
  font-size: 15px;
  opacity: 1;
}

.search-input.form-control {
  border-radius: 3em;
  padding: 1.2em;
}

.search-icon {
  width: 16px;
  height: 16px;
  position: absolute;
  right: 15px;
  top: 30%;
  margin-left: 0.5em;
}
</style>
