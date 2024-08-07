<template>
  <div
    v-if="!isEmbed"
    id="sidebar-container"
    ref="sidebarContainer"
    class="sidebar-container"
    :class="{ 'sidebar-arts-container': showSidePanel }"
  >
    <div class="sidebarRelative position-relative">
      <div class="sidebar-desktop position-relative">
        <div class="sidebar-header">
          <Logo class="cursor-pointer" :logo-alt="1"></Logo>
        </div>
        <div class="sidebar-body">
          <div v-if="this.$route.name !== 'index-grants'" class="sidebar-tabs">
            <b-nav tabs fill>
              <b-nav-item
                v-for="tab in navigationTabs"
                :key="tab.id"
                :active="active === tab.name ? true : false"
                :class="tab.name | lowerCase"
                @click.prevent="handleNavigation($event, tab.name)"
                >{{ tab.name }}
              </b-nav-item>
            </b-nav>
          </div>
          <div class="sidebar-content">
            <slot name="content"></slot>
            <slot name="badges"></slot>
            <slot name="cards"></slot>
            <transition v-if="showLoading" name="fade">
              <div class="loading-spinner">
                <img src="@/assets/images/loading.gif" />
              </div>
            </transition>
          </div>
          <Contact
            :subject="
              `FPCC Map: Didn't find what I was looking for (${$route.path})`
            "
          ></Contact>
        </div>
        <div
          v-if="showSidePanel"
          class="sidebar-side-panel"
          :class="{ 'hide-scroll-y': showGallery }"
        >
          <slot name="side-panel"></slot>
        </div>
      </div>
      <div class="sidebar-mobile d-none">
        <SideBarFold>
          <template v-slot:side-panel>
            <div
              v-if="showSidePanel"
              class="sidebar-side-panel"
              :class="{ 'hide-scroll-y': showGallery }"
            >
              <slot name="side-panel"></slot>
            </div>
          </template>
          <template v-slot:tabs>
            <div v-show="$route.name !== 'index-grants'" class="sidebar-tabs">
              <b-nav tabs fill>
                <b-nav-item
                  v-for="tab in navigationTabs"
                  :key="tab.id"
                  :active="active === tab.name ? true : false"
                  :class="tab.name | lowerCase"
                  @click.prevent="handleNavigation($event, tab.name)"
                  >{{ tab.name }}
                </b-nav-item>
              </b-nav>
            </div>
          </template>
          <template v-slot:badges>
            <slot name="badges"></slot>
          </template>
          <slot name="cards"></slot>
        </SideBarFold>
      </div>
    </div>
    <ScrollDownIndicator
      :desktop-container="'#sidebar-container'"
      :mobile-container="'#side-inner-collapse'"
    ></ScrollDownIndicator>
  </div>
</template>

<script>
import Logo from '@/components/Logo.vue'
import SideBarFold from '@/components/SideBarFold.vue'
import Contact from '@/components/Contact.vue'
import ScrollDownIndicator from '@/components/ScrollDownIndicator.vue'

export default {
  components: {
    Logo,
    SideBarFold,
    Contact,
    ScrollDownIndicator
  },
  filters: {
    lowerCase(value) {
      return value.toLowerCase()
    }
  },
  props: {
    active: {
      type: String,
      default: ''
    },
    badgesToDisplay: {
      type: Array,
      default() {
        return []
      }
    },
    showSidePanel: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      navigationTabs: [
        {
          id: 0,
          name: 'Languages',
          path: '/languages',
          pathName: 'index-languages-language'
        },
        {
          id: 1,
          name: 'Arts',
          path: '/art',
          pathName: 'index-art-art'
        },
        {
          id: 2,
          name: 'Heritage',
          path: '/heritages',
          pathName: 'index-heritages-heritage'
        }
      ],
      fold: true
    }
  },
  computed: {
    showLoading() {
      return this.$store.state.sidebar.showLoading
    },
    showGallery() {
      return this.$store.state.sidebar.showGallery
    }
  },

  methods: {
    handleNavigation(e, data) {
      // Recalibrate Vuex Values
      this.resetState()

      const path = this.navigationTabs.find(nt => nt.name === data).path
      this.$router.push({
        path
      })

      if (this.$route.name === 'index-art') {
        this.$store.commit('arts/setFilter', 'artwork')
      }
    },

    toggleFold(e) {
      this.fold = !this.fold
    },
    resetState() {
      this.$store.commit('arts/setTaxonomyTag', [])
      this.$store.commit('arts/setArtSearch', '')
      this.$store.commit('sidebar/setDrawerContent', false)
    }
  }
}
</script>

<style>
.sidebar-container {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: var(--sidebar-width, 425px);
  overflow-y: scroll;
  padding-bottom: 1em;
}

.sidebar-arts-container {
  width: var(--sidebar-width, 425px);
}

.sidebar-header {
  background-color: transparent;
  overflow-x: hidden;
}

.sidebar-body {
  background-color: white;
}
.nav-tabs {
  display: flex;
  border-bottom: 0;
}

.nav-tabs .nav-item {
  flex: 1;
}
.nav-tabs .nav-link {
  font-family: 'Faustina', serif;
  font-size: 15px;
  font-weight: 500;
  background-color: #03333a;
  color: #fff;
  border-top-left-radius: 0rem;
  border-top-right-radius: 0rem;
}
.nav-tabs .nav-link.active {
  color: #b47a2b;
  position: relative;
  font-weight: 700;
  border: 0;
  opacity: 1;
  text-transform: capitalize !important;
}

.sidebar-desktop .nav-tabs .nav-link.active::before {
  content: '';
  display: block;
  width: 100%;
  height: 10px;
  background-color: white;
  position: absolute;
  top: -10px;
  left: 0;
  border-top-right-radius: 0.5em;
}

.sidebar-desktop .nav-tabs .nav-item.arts .nav-link.active::before {
  border-top-left-radius: 0.5em;
}
.sidebar-desktop .nav-tabs .nav-item.heritage .nav-link.active::before {
  border-top-left-radius: 0.5em;
  border-top-right-radius: 0em;
}

@media (max-width: 992px) {
  .sidebar-desktop {
    display: none;
  }

  .sidebar-container {
    width: 100%;
    top: unset;
    padding: 0;
    margin: 0;
    z-index: 50;
    max-height: 80%;
    overflow-y: unset;
  }

  .scroll-indicator-container {
    width: 100%;
  }

  .sidebar-mobile {
    display: block !important;
  }

  .sidebar-mobile .sidebar-tabs {
    margin-top: 10px;
    background-color: white;
  }

  .sidebar-mobile .sidebar-tabs ul li {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f4eee9;
    height: 50px;
  }

  .sidebar-mobile .sidebar-tabs ul .nav-link {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
  }

  .sidebar-mobile .sidebar-tabs ul .nav-link.active {
    border-radius: 0;
  }

  .sidebar-tabs-fold {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
  }

  .sidebar-tabs-fold .nav-tabs .nav-link {
    opacity: 1;
  }

  .sidebar-tabs-fold .nav-fill .nav-item {
    background-color: white;
  }

  .nav-tabs .nav-link .active {
    border: 0;
  }

  .sidebar-container .sidebar-side-panel {
    position: fixed;
    top: 0;
    left: 0;
    width: 400px;
    height: 100vh;
    overflow-x: hidden;
    z-index: 999999;
    background: #f9f9f9 0% 0% no-repeat padding-box;
    box-shadow: 0px 3px 6px #00000029;
  }

  .sidebar-container .arts-right-panel {
    width: 400px;
    height: 100vh;
  }

  .sidebar-container .panel-close-btn {
    display: absolute !important;
  }
}

.loading-spinner {
  display: flex;
  justify-content: center;
  width: 100%;
}

.loading-spinner img {
  width: 75px;
  height: 75px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
