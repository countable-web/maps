<template>
  <div class="grants-main-container">
    <SideBar v-if="this.$route.name === 'index-grants'" active="Grants">
      <template v-slot:badges>
        <div class="grants-header">
          <span class="title">Grants</span>
          <img src="@/assets/images/graph_background_grants.svg" />
          <div class="grant-header-more" @click.prevent="handleReturn">
            <img class="ml-1" src="@/assets/images/return_icon_hover.svg" />
            <span class="ml-1 font-weight-bold">Return</span>
          </div>
        </div>
        <section class="pl-3 pr-3 mt-3">
          <Accordion
            class="no-scroll-accordion hide-mobile"
            :content="accordionContent"
          ></Accordion>
        </section>
        <hr class="sidebar-divider" />
        <CardFilter class="mt-3 mb-3" :mode="'grants'" />
        <hr class="sidebar-divider" />
        <GrantFilter :max-date="getMaxDate" :min-date="getMinDate" class="mb-2">
          <template v-slot:badge-filter>
            <span class="sidebar-title">FPCC Departments</span>
            <section
              id="badge-list-container"
              class="badge-list-container mt-3"
            >
              <BadgeFilter
                v-for="badge in grantBadges"
                :key="`badge-grant-${badge.name}`"
                class="mt-2 cursor-pointer"
                :color="badge.color"
                :child-taxonomy="badge.id ? getChildCategory(badge.name) : []"
                :is-selected="filterMode === badge.name.toLowerCase()"
                :filter-type="'grants'"
              >
                <template v-slot:badge>
                  <Badge
                    :content="badge.name === 'All' ? 'All Grants' : badge.name"
                    :number="
                      badge.name === 'All'
                        ? visibleGrantsCount
                        : getCountValues(badge.name.toLowerCase())
                    "
                    :bgcolor="badge.color"
                    :pill-shape="true"
                    :mode="getBadgeStatus(filterMode, badge.name.toLowerCase())"
                    @click.native.prevent="
                      badgeClick($event, badge.name.toLowerCase())
                    "
                  ></Badge>
                </template>
              </BadgeFilter>
            </section>
          </template>
        </GrantFilter>
      </template>
      <template v-slot:cards>
        <section class="pl-3 pr-3">
          <b-row v-if="paginatedGrants.length !== 0">
            <b-col
              v-for="(grant, index) in paginatedGrants"
              :key="`grants-item-${index}`"
              lg="12"
              xl="12"
              md="12"
              sm="12"
              class="mt-3 hover-left-move"
            >
              <GrantsCard
                :grant="grant"
                :parent-tag-object="getParentTag(grant)"
                :is-selected="currentGrant && currentGrant.id === grant.id"
              ></GrantsCard>
            </b-col>
          </b-row>
          <b-row
            v-else-if="
              paginatedGrants.length === 0 &&
                (isGrantsSearchMode || isCategoryFilterMode)
            "
            class="search-empty-container"
          >
            <img src="@/assets/images/search_icon.svg" />
            Sorry, no results found. Please adjust your filters and try again.
          </b-row>
        </section>
      </template>
    </SideBar>

    <div v-else-if="this.$route.name === 'index-grants-grants'">
      <div>
        <nuxt-child />
      </div>
    </div>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue'
import Accordion from '@/components/Accordion.vue'
import GrantsCard from '@/components/grants/GrantsCard.vue'
import GrantFilter from '@/components/grants/GrantsFilter.vue'
import Badge from '@/components/Badge.vue'
import BadgeFilter from '@/components/BadgeFilter.vue'
import CardFilter from '@/components/CardFilter.vue'

export default {
  components: {
    SideBar,
    GrantFilter,
    Accordion,
    GrantsCard,
    Badge,
    BadgeFilter,
    CardFilter
  },
  head() {
    return {
      meta: [
        {
          name: 'google-site-verification',
          content: 'wWf4WAoDmF6R3jjEYapgr3-ymFwS6o-qfLob4WOErRA'
        }
      ]
    }
  },
  data() {
    return {
      mode: 'All',
      accordionContent: `
          In pursuit of a vision where our languages, arts, and cultures are thriving and valued by everyone, our Indigenous-led Crown Corporation provides grants, training, coaching and resources to communities. To apply for grants, please visit our website at https://fpcc.ca/grants/ To access information on grants awarded since 2014, use the search bar or filters below, or browse locations on the map. <br/> <br/>

          <div id="grants-list-collapse" class="collapse-item">
            <b><span class="collapse-icon">&#9658;</span> List of Grants</b>
          </div>

          <ul id="grants-list-collapse-content" class="collapse-item-content">
            <li>ARTS - Arts One Time Grant</li>
            <li>AIND - Individual Artists Grant</li>
            <li>ASHR - Sharing Traditional Arts Grant</li>
            <li>AORG - Organizations and Collectives Grant</li>
            <li>AADM - Arts Administration Internships Grant</li>
            <li>AMIC - Arts Micro Grants</li>
            <li>AIAPS - Indigenous Arts Scholarship</li>
            <li>AIAPC - Community Arts Spaces</li>
            <li>ALND - Community Land Based Arts Grant</li>
            <li>AEMIP - Emerging Music Industry Professionals Grant</li>
            <li>AECMR - Expanding Capacity in the Indigenous Music Recording Industry Grant</li>
            <li>ATPMP - Touring, Promotion/Marketing and Performance Grant</li>
            <li>AIMIR - Indigenous Music Recording Industry</li>
            
            <li>HMIC - Indigenous Heritage Micro Grant</li>
            <li>HSOP - Sense of Place Grant</li>
            <li>HERIT - Heritage Grant</li>
            <li>HERIT - Oral Histories Program</li>
            <li>HERIT - Heritage Branch Pilot Project</li>
            <li>HERIT - Climate Change Pilot Project</li>
            <li>HERIT - Indigenous Cultural Heritage Infrastructure Grant</li>
            <li>HERIT - Cultural Heritage Stewardship Grant</li>
            <li>HERIT - Place Names Pilot Project</li>
            <li>HHSP - Heritage Stewardship Program</li>
            <li>HHIP - Heritage Infrastructure Program</li>
            <li>HBKG - Braided Knowledge Grant</li>

            <li>LALI - Aboriginal Languages Initiative</li>
            <li>LBCLI - BC Language Initiative</li>
            <li>LDIGI - Digitization Program</li>
            <li>LFV - FirstVoices Program</li>
            <li>LILG - Indigenous Languages Grant</li>
            <li>LANG - Language One Time Grant</li>
            <li>LLN - Language Nest Program</li>
            <li>LLRPP - Language Revitalization Planning Program</li>
            <li>LMAP - Mentor-Apprentice Program</li>
            <li>LPATH - Pathways to Language Vitality Program</li>
            <li>LRML - Reclaiming My Language Program</li>
            <li>LTECH - Language Technology Program</li>
            <li>LYES - Youth Empowered Speakers Program</li>
          </ul>


          <div id="partner-list-collapse" class="collapse-item">
            <b><span class="collapse-icon">&#9658;</span> Funding Partner Acknowledgements</b>
          </div>

          <div id="partner-list-collapse-content" class="collapse-item-content">
            <span style="margin: 1em 0;">The key funding partners for each department are as follows:</span> <br/>

            <div style="font-weight: 700;">Arts</div>

            <ul>
              <li>BC Arts Council </li>
              <li>Creative BC </li>
              <li> Margaret A. Cargill Philanthropies</li>
            </ul>

            <div style="font-weight: 700;">Heritage</div>

            <ul>
              <li>Heritage Branch, Ministry of Forests, Lands, Natural Resource Operations & Rural Development, Province of British Columbia </li>
              <li>Ministry of Environment & Climate Action Strategy, Province of British Columbia</li>
              <li>Indigenous Services Canada, Government of Canada </li>
            </ul>

            <div style="font-weight: 700;">Language</div>

            <ul>
              <li> Aboriginal Neighbours</li>
              <li> Canadian Heritage, Government of Canada</li>
              <li> First Peoples’ Cultural Foundation</li>
              <li>Ministry of Indigenous Relations and Reconciliation, Province of British Columbia </li>
              <li>RSF Social Finance</li>
            </ul>
          </div>


         `,
      maximumLength: 0,
      grantBadges: [
        {
          name: 'All',
          color: '#99281C'
        },
        {
          id: 1,
          name: 'Arts',
          color: '#2C8190'
        },
        {
          id: 2,
          name: 'Heritage',
          color: '#6D4264'
        },
        {
          id: 3,
          name: 'Language',
          color: '#B47A2B'
        }
      ]
    }
  },
  beforeRouteLeave(to, from, next) {
    this.$root.$emit('resetMap')
    this.resetGrantFilter()
    next()
  },
  computed: {
    filterMode() {
      return this.$store.state.grants.grantFilterMode
    },
    getCategoryFilterList() {
      return this.$store.state.grants.grantCategoryList
    },
    grantsSearchQuery() {
      return this.$store.state.grants.grantsSearch
    },
    visibleGrantsCount() {
      return this.$store.state.grants.visibleGrantsCount
    },
    isGrantsSearchMode() {
      return this.grantsSearchQuery.length !== 0
    },
    isCategoryFilterMode() {
      return this.getCategoryFilterList.length !== 0
    },
    isMobile() {
      return this.$store.state.responsive.isMobileSideBarOpen
    },
    grants() {
      return this.$store.state.grants.grantsSet
    },
    grantsGeo() {
      return this.$store.state.grants.grantsGeo
    },
    getMinDate() {
      let getMinimum = 0
      this.grants.forEach(grant => {
        const grantYear = grant.properties.year
        getMinimum =
          getMinimum !== 0
            ? getMinimum < grant.properties.year
              ? getMinimum
              : grantYear
            : grant.properties.year
      })
      return getMinimum
    },
    getMaxDate() {
      let getMaximum = 0
      this.grants.forEach(grant => {
        const grantYear = grant.properties.year
        getMaximum =
          getMaximum !== 0
            ? getMaximum > grantYear
              ? getMaximum
              : grantYear
            : grantYear
      })

      // Grants' duration is always a year's length,
      // so the max date is always max year + 1
      return getMaximum + 1
    },
    grantsTypeList() {
      if (this.filterMode === 'all') {
        return this.grants
      } else {
        return this.grants.filter(grant => {
          return (
            grant.properties.category &&
            this.getCategoryId(grant.properties.category).parent ===
              this.getCategoryId(this.filterMode).id
          )
        })
      }
    },
    getGrantList() {
      //  if year filtermode is activated
      if (
        this.getGrantsDateFilter ||
        this.isCategoryFilterMode ||
        this.isGrantsSearchMode
      ) {
        let finalGrants = []
        const { fromDate, toDate } = this.getGrantsDateFilter
        const filteredYear = this.grantsTypeList.filter(grant => {
          return (
            grant.properties.year <= toDate && grant.properties.year >= fromDate
          )
        })

        // Filter by categories
        if (this.isCategoryFilterMode) {
          finalGrants = filteredYear.filter(grant => {
            const isCategoryFound = this.getCategoryFilterList.some(
              tag =>
                tag.toLowerCase() === grant.properties.category.toLowerCase()
            )
            return isCategoryFound
          })
        } else {
          finalGrants = filteredYear
        }

        // Filter by Search Query
        if (this.isGrantsSearchMode) {
          const grantsSearchResult = finalGrants.filter(grant => {
            return (
              grant.properties.grant
                .toLowerCase()
                .includes(this.grantsSearchQuery.toLowerCase()) ||
              grant.properties.recipient
                .toLowerCase()
                .includes(this.grantsSearchQuery.toLowerCase()) ||
              grant.properties.category
                .toLowerCase()
                .includes(this.grantsSearchQuery.toLowerCase())
            )
          })
          this.$root.$emit('updateGrantsMarkers', grantsSearchResult)
          return grantsSearchResult
        } else {
          this.$root.$emit('updateGrantsMarkers', finalGrants)
          return finalGrants
        }
      } else {
        this.$root.$emit('updateGrantsMarkers', this.grantsTypeList)
        return this.grantsTypeList
      }
    },
    paginatedGrants() {
      return this.getGrantList.slice(0, this.maximumLength)
    },
    getGrantsDateFilter() {
      return this.$store.state.grants.filterDate
    },
    categoryList() {
      return this.$store.state.grants.categorySearchSet
    },
    currentGrant() {
      return this.$store.state.grants.currentGrant
    }
  },
  created() {
    this.$root.$emit('resetMap')
  },
  mounted() {
    this.$eventHub.whenMap(map => {
      this.$root.$emit('toggleMapLayers')
    })

    this.$store.commit('sidebar/toggleLoading', true)
    this.$store.commit('sidebar/setScrollIndicatorValue', false)

    setTimeout(() => {
      this.$store.commit('sidebar/toggleLoading', false)
    }, 3000)

    // Trigger addeventlistener only if there's Sidebar, used for Pagination
    if (this.$route.name === 'index-grants' && !this.isEmbed) {
      const mobileContainer = document.querySelector('#side-inner-collapse')
      const desktopContainer = document.querySelector('#sidebar-container')

      const containerArray = [mobileContainer, desktopContainer]

      containerArray.forEach(elem => {
        elem.addEventListener('scroll', e => {
          if (
            elem.scrollTop + elem.clientHeight >= elem.scrollHeight - 50 &&
            elem.scrollTop !== 0
          ) {
            if (this.getGrantList.length > this.maximumLength) {
              this.loadMoreData()
            }
          }
        })
      })
      this.loadMoreData()
    }
  },
  methods: {
    toggleLayer() {
      this.$eventHub.whenMap(map => {
        this.$root.$emit('toggleMapLayers')
      })
    },
    handleReturn() {
      this.$router.push({
        path: '/languages'
      })
    },
    loadMoreData() {
      this.$store.commit('sidebar/toggleLoading', true)
      setTimeout(() => {
        this.maximumLength += 16
        this.$store.commit('sidebar/toggleLoading', false)
        setTimeout(() => {
          this.$root.$emit('triggerScrollVisibilityCheck')
        }, 500)
      }, 250)
    },
    getCategoryId(name) {
      return this.categoryList.find(
        category => category.name.toLowerCase() === name.toLowerCase()
      )
    },
    getParentTag(grant) {
      return grant.properties.category
        ? this.getParentName(
            this.getCategoryId(grant.properties.category).parent
          )
        : { color: '#9A281B' }
    },
    getParentName(childCateg) {
      return this.grantBadges.find(
        badge =>
          this.categoryList.find(category => category.id === childCateg)
            .name === badge.name
      )
    },
    getChildCategory(name) {
      return this.categoryList
        .filter(category => category.parent === this.getCategoryId(name).id)
        .sort((a, b) => {
          return a.order - b.order
        })
    },
    getCountValues(type) {
      return (this.getGrantsDateFilter || this.categoryList) &&
        this.filterMode === type
        ? this.filterArray(this.getGrantList, type)
        : this.filterArray(this.grants, type)
    },
    filterArray(grantArray, type) {
      return grantArray.filter(
        category =>
          category.properties.category &&
          this.getCategoryId(category.properties.category).parent ===
            this.getCategoryId(type).id
      ).length
    },
    badgeClick($event, name) {
      this.maximumLength = 7
      this.handleBadge($event, name)
      this.resetGrantFilter()
    },
    resetGrantFilter() {
      const resetList = this.categoryList.map(category => {
        category.isChecked = false
        return category
      })
      this.$store.commit('grants/setGrantCategorySearchSet', resetList)
      this.$store.commit('grants/setCategoryTag', [])
      // Reset text filter
      this.$store.commit('grants/setGrantsSearch', '')
      this.$root.$emit('clearInput')
    }
  }
}
</script>
<style></style>
