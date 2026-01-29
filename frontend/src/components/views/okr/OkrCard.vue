<template>
  <el-card :body-style="{ padding: '10px', overflow: 'visible', width: '100%', minWidth: '0' }" style="margin-bottom: 10px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06); transition: all 0.3s; overflow: visible; width: 100%; min-width: 0;">
    <div style="width: 100%;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px;">
        <div style="flex: 1;">
          <div v-if="props.createdDate" style="display: inline-block; padding: 2px 4px; background-color: #F5F7FA; border-radius: 4px; font-size: 10px; color: #909399; margin-bottom: 4px;">
            {{ props.createdDate }}
          </div>
          <div v-else style="display: inline-block; padding: 2px 4px; background-color: #F5F7FA; border-radius: 4px; font-size: 10px; color: #909399; margin-bottom: 4px;">
            2026-01-01
          </div>
          <h3 style="margin: 0 0 6px 0; font-size: 17px; font-weight: 600; color: #303133;">{{ objective }}</h3>
          <div style="display: flex; align-items: center; gap: 6px;">
            <div style="display: flex; align-items: center; gap: 3px;">
              <span style="font-size: 12px; color: #909399;">负责人:</span>
              <span style="font-size: 12px; color: #606266; font-weight: 500;">{{ owner }}</span>
              <el-icon 
                @click="props.toggleFollow(props.ownerId, props.owner)"
                :style="{
                  color: props.isFollowed(props.ownerId) ? '#FFD700' : '#C0C4CC',
                  fontSize: '14px',
                  cursor: 'pointer',
                  transition: 'all 0.3s',
                  marginLeft: '4px'
                }"
                :title="props.isFollowed(props.ownerId) ? '取消关注' : '关注'"
              >
                <Star :fill="props.isFollowed(props.ownerId) ? '#FFD700' : 'none'" />
              </el-icon>
            </div>
            <div 
              style="position: relative; display: inline-block;"
              @mouseenter="scoreHoverVisible[0] = true"
              @mouseleave="scoreHoverVisible[0] = false"
            >
              <div 
                :style="{
                  padding: '2px 6px',
                  backgroundColor: '#ecf5ff',
                  color: '#409EFF',
                  borderRadius: '6px',
                  fontSize: '11px',
                  fontWeight: '500',
                  cursor: 'pointer',
                  transition: 'all 0.3s',
                  border: scoreHoverVisible[0] ? '1px solid #409EFF' : '1px solid transparent'
                }"
                @click="editTotalScore = true"
              >
                总分: {{ editTotalScore ? '' : formatScore(localTotalScore) }}
                <input 
                  v-if="editTotalScore"
                  v-model.number="localTotalScore"
                  type="number"
                  min="0"
                  max="5"
                  step="0.1"
                  @blur="editTotalScore = false"
                  @keyup.enter="editTotalScore = false"
                  style="width: 30px; margin-left: 2px; padding: 1px 2px; border: 1px solid #409EFF; border-radius: 3px; font-size: 11px; text-align: center;"
                  autofocus
                />
              </div>
            </div>
          </div>
        </div>
        <div style="display: flex; align-items: center; gap: 4px;">
          <span style="font-size: 13px; font-weight: 600; color: #409EFF;">{{ totalProgress }}%</span>
          <el-progress :percentage="totalProgress" :stroke-width="5" :color="'#409EFF'" :show-text="false" style="width: 80px;" />
        </div>
      </div>
      

      <div style="margin-bottom: 10px; padding: 6px; background-color: #F5F7FA; border-radius: 4px; position: relative; z-index: 1;">
        <h4 style="margin: 0 0 10px 0; font-size: 13px; font-weight: 600; color: #303133;">参与人员</h4>
        <div style="display: flex; align-items: center; gap: 6px; overflow: visible; flex-wrap: wrap;">
          <div v-for="(participant) in visibleParticipants" :key="participant.id"
               style="position: relative; cursor: pointer; flex-shrink: 0; z-index: 10;"
               @mouseenter="showParticipantInfo(participant)"
               @mouseleave="startHideTimer"
               @click="$emit('select-participant', participant)">
            <div style="display: flex; align-items: center; gap: 2px; padding: 2px 4px; background-color: #FFFFFF; border: 1px solid #E4E7ED; border-radius: 10px; transition: all 0.2s; cursor: pointer;">
              <el-avatar :size="16" :src="participant.avatar" />
              <div>
                <div style="font-size: 10px; font-weight: 500; color: #303133;">{{ participant.name }}</div>
                <div style="font-size: 8px; color: #909399;">{{ participant.role }}</div>
              </div>
            </div>
            
            <div v-if="hoveredParticipant?.id === participant.id" 
                 @mouseenter="cancelHideTimer"
                 @mouseleave="startHideTimer"
                 style="position: absolute; top: 100%; left: 0; margin-top: 6px; z-index: 99999; min-width: 240px; padding: 10px; background-color: #FFFFFF; border: 1px solid #E4E7ED; border-radius: 6px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); transition: all 0.2s; opacity: 1; transform: translateY(0);">
              <div style="position: absolute; top: -5px; left: 18px; width: 0; height: 0; border-left: 5px solid transparent; border-right: 5px solid transparent; border-bottom: 5px solid #FFFFFF;"></div>
              <div style="position: absolute; top: -6px; left: 17px; width: 0; height: 0; border-left: 6px solid transparent; border-right: 6px solid transparent; border-bottom: 6px solid #E4E7ED;"></div>
              <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px; padding-bottom: 6px; border-bottom: 1px solid #E4E7ED;">
                <el-avatar :size="32" :src="participant.avatar" />
                <div style="flex: 1;">
                  <div style="font-size: 13px; font-weight: 600; color: #303133;">{{ participant.name }}</div>
                  <div style="font-size: 11px; color: #909399;">{{ participant.role }}</div>
                  <div style="font-size: 10px; color: #409EFF; margin-top: 3px;">
                    总进度: {{ getParticipantTotalProgress(participant.tasks || []) }}%
                  </div>
                </div>
              </div>
              <div style="font-size: 11px; line-height: 1.4;">
                <div style="margin-bottom: 4px; color: #606266; font-weight: 500;">负责任务:</div>
                <div v-if="getParticipantTasks(participant.id).length > 0" style="line-height: 1.5;">
                  <div v-for="task in getParticipantTasks(participant.id)" :key="task.id" style="margin-bottom: 5px; padding: 5px; background-color: #F5F7FA; border-radius: 4px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
                      <span style="font-size: 10px; font-weight: 500; color: #303133;">{{ task.title }}</span>
                      <span style="font-size: 9px; color: #67C23A; font-weight: 600;">{{ task.progress }}%</span>
                    </div>
                    <div style="margin-top: 2px; padding-left: 8px;">
                      <div v-for="subtask in task.subtasks" :key="subtask.id" style="font-size: 9px; color: #909399; margin-bottom: 1px; display: flex; justify-content: space-between;">
                        <span>{{ subtask.title }}</span>
                        <span style="color: #606266;">{{ subtask.progress }}%</span>
                      </div>
                    </div>
                  </div>
                </div>
                <div v-else style="color: #909399; font-size: 10px;">暂无具体任务</div>
              </div>
            </div>
          </div>
          
          <div v-if="hiddenParticipants.length > 0"
               style="flex-shrink: 0; cursor: pointer;"
               @click="showAllParticipants = true">
            <div style="padding: 3px 8px; color: #409EFF; font-size: 11px; cursor: pointer; transition: all 0.2s;">
              更多 ({{ hiddenParticipants.length }})
            </div>
          </div>
        </div>
      </div>
      
      <div style="margin-top: 12px;">
        <div v-for="(kr, index) in localKeyResults" :key="index" 
             style="margin-bottom: 4px; padding: 5px; border: 1px solid #E4E7ED; border-radius: 6px; background-color: #FFFFFF; transition: all 0.3s; position: relative;">
          <div style="display: flex; justify-content: space-between; align-items: center; gap: 10px; flex-wrap: wrap;">
            <div style="flex: 1;">
              <span style="font-size: 13px; font-weight: 500; color: #303133;">{{ kr.title }}</span>
            </div>
            <div style="display: flex; align-items: center; gap: 14px;">
              <div style="display: flex; flex-direction: column; align-items: center; position: relative;" data-progress-section>
                <span style="font-size: 11px; color: #909399; margin-bottom: 3px;">进度</span>
                <div 
                  style="display: flex; align-items: center; gap: 5px; cursor: pointer; transition: all 0.3s;"
                  @click="openProgressDialog(index)"
                  @mouseenter="progressHoverVisible[index] = true"
                  @mouseleave="progressHoverVisible[index] = false"
                >
                  <el-progress :percentage="kr.progress" :stroke-width="4" :color="getProgressColorByStatus(kr.status)" :show-text="false" style="width: 65px;" />
                  <span :style="{ fontSize: '12px', fontWeight: '600', color: getProgressTextColor(kr.status) }">{{ kr.progress }}%</span>
                </div>
                <!-- 进度编辑弹窗 -->
                <div v-if="progressDialogVisible[index]" 
                     data-progress-dialog
                     style="position: absolute; top: 100%; left: 50%; transform: translateX(-50%); margin-top: 5px; z-index: 99999; min-width: 240px; padding: 10px; background-color: #FFFFFF; border: 1px solid #E4E7ED; border-radius: 6px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); transition: all 0.2s; opacity: 1; transform: translateY(0) translateX(-50%);">
                  <!-- 弹窗箭头 -->
                  <div style="position: absolute; top: -5px; left: 50%; transform: translateX(-50%); border-left: 5px solid transparent; border-right: 5px solid transparent; border-bottom: 5px solid #FFFFFF;"></div>
                  <div style="position: absolute; top: -6px; left: 50%; transform: translateX(-50%); border-left: 6px solid transparent; border-right: 6px solid transparent; border-bottom: 6px solid #E4E7ED;"></div>
                  
                  <!-- 进度编辑部分 -->
                  <div style="margin-bottom: 8px; padding-bottom: 6px; border-bottom: 1px solid #E4E7ED;">
                    <h3 style="margin: 0 0 6px 0; font-size: 13px; font-weight: 600; color: #303133;">当前进度</h3>
                    <div style="display: flex; align-items: center; gap: 6px;">
                      <el-progress :percentage="tempProgress" :stroke-width="4" :color="getProgressColorByStatus(tempStatus)" :show-text="false" style="width: 65px;" />
                      <input 
                        v-model.number="tempProgress"
                        type="number"
                        min="0"
                        max="100"
                        style="width: 50px; padding: 3px 6px; border: 1px solid #E4E7ED; border-radius: 3px; font-size: 12px; text-align: center;"
                      />
                      <span style="font-size: 12px; color: #606266;">%</span>
                    </div>
                  </div>
                  
                  <!-- 状态选择部分 -->
                  <div style="margin-bottom: 8px;">
                    <h3 style="margin: 0 0 6px 0; font-size: 13px; font-weight: 600; color: #303133;">状态</h3>
                    <div style="display: flex; gap: 6px;">
                      <div 
                        :style="{
                          flex: '1',
                          padding: '6px',
                          border: '1px solid',
                          borderRadius: '4px',
                          cursor: 'pointer',
                          backgroundColor: tempStatus === 'normal' ? '#f0f9eb' : '#FFFFFF',
                          borderColor: tempStatus === 'normal' ? '#67C23A' : '#E4E7ED',
                          color: tempStatus === 'normal' ? '#67C23A' : '#606266'
                        }"
                        @click="tempStatus = 'normal'"
                      >
                        <div style="font-size: 12px; font-weight: 500; color: #67C23A;">正常</div>
                      </div>
                      <div 
                        :style="{
                          flex: '1',
                          padding: '6px',
                          border: '1px solid',
                          borderRadius: '4px',
                          cursor: 'pointer',
                          backgroundColor: tempStatus === 'risk' ? '#fef0f0' : '#FFFFFF',
                          borderColor: tempStatus === 'risk' ? '#F56C6C' : '#E4E7ED',
                          color: tempStatus === 'risk' ? '#F56C6C' : '#606266'
                        }"
                        @click="tempStatus = 'risk'"
                      >
                        <div style="font-size: 12px; font-weight: 500; color: #F56C6C;">有风险</div>
                      </div>
                      <div 
                        :style="{
                          flex: '1',
                          padding: '6px',
                          border: '1px solid',
                          borderRadius: '4px',
                          cursor: 'pointer',
                          backgroundColor: tempStatus === 'delayed' ? '#f4e4ff' : '#FFFFFF',
                          borderColor: tempStatus === 'delayed' ? '#9C27B0' : '#E4E7ED',
                          color: tempStatus === 'delayed' ? '#9C27B0' : '#606266'
                        }"
                        @click="tempStatus = 'delayed'"
                      >
                        <div style="font-size: 12px; font-weight: 500; color: #9C27B0;">已延期</div>
                      </div>
                    </div>
                  </div>
                  
                  <!-- 操作按钮 -->
                  <div style="display: flex; gap: 6px; justify-content: flex-end;">
                    <button 
                      @click="progressDialogVisible[index] = false"
                      style="padding: 5px 10px; background: #FFFFFF; color: #606266; border: 1px solid #E4E7ED; border-radius: 4px; font-size: 12px; cursor: pointer; transition: all 0.2s;"
                    >
                      取消
                    </button>
                    <button 
                      @click="saveProgress"
                      style="padding: 5px 10px; background: #409EFF; color: white; border: none; border-radius: 4px; font-size: 12px; cursor: pointer; transition: all 0.2s;"
                    >
                      确认
                    </button>
                  </div>
                </div>
              </div>
              <div style="display: flex; flex-direction: column; align-items: center; position: relative;">
                <span style="font-size: 11px; color: #909399; margin-bottom: 3px;">权重</span>
                <!-- 错误提示：只在当前正在编辑的框上边显示 -->
                <div v-if="weightError && index === currentEditingIndex" 
                     style="position: absolute; top: -10px; left: 50%; transform: translateX(-50%); text-align: center; z-index: 10;">
                  <span style="font-size: 12px; color: #F56C6C; font-weight: 500; background-color: #FFFFFF; padding: 2px 8px; border-radius: 3px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #FBC4C4; white-space: nowrap;">总权重不得超过100%</span>
                </div>
                <div v-if="index < localKeyResults.length - 1" 
                     style="display: flex; align-items: center; gap: 3px;">
                  <input 
                    :value="kr.weight" 
                    @input="onWeightInput(index, $event)"
                    @change="adjustWeights(index)"
                    @mouseenter="weightHoveredIndex = index"
                    @mouseleave="weightHoveredIndex = -1"
                    type="number"
                    min="0"
                    max="100"
                    :style="{
                      width: '50px',
                      padding: '4px 6px',
                      border: weightHoveredIndex === index ? '1px solid #409EFF' : '1px solid transparent',
                      borderRadius: '4px',
                      fontSize: '13px',
                      textAlign: 'center',
                      transition: 'all 0.3s',
                      MozAppearance: 'textfield',
                      appearance: 'textfield'
                    }"
                  />
                  <span style="font-size: 12px; color: #606266;">%</span>
                </div>
                <div v-else 
                     @mouseenter="fixedWeightHovered = true"
                     @mouseleave="fixedWeightHovered = false"
                     :style="{
                       display: 'flex',
                       alignItems: 'center',
                       gap: '4px',
                       position: 'relative',
                       cursor: 'not-allowed',
                       padding: '4px 6px',
                       border: fixedWeightHovered ? '1px solid #E4E7ED' : '1px solid transparent',
                       borderRadius: '4px',
                       transition: 'all 0.3s',
                       width: '50px',
                       justifyContent: 'center'
                     }"
                  >
                  <span style="font-size: 12px; font-weight: 600; color: #E6A23C; text-align: center;">{{ kr.weight }}%</span>
                  <el-tooltip content="你可以通过更改其他keyResult的形式更改此权重" placement="top" effect="dark">
                    <span style="font-size: 11px; color: #909399; cursor: help;">ℹ️</span>
                  </el-tooltip>
                </div>
              </div>
              <div style="display: flex; flex-direction: column; align-items: center; position: relative;">
                <span style="font-size: 11px; color: #909399; margin-bottom: 3px;">评分</span>
                <div 
                  :style="{
                    padding: '3px 10px',
                    borderRadius: '8px',
                    fontSize: '12px',
                    fontWeight: '600',
                    cursor: 'pointer',
                    transition: 'all 0.3s',
                    border: scoreHoverVisible[index] ? '1px solid #409EFF' : '1px solid transparent',
                    backgroundColor: scoreHoverVisible[index] ? '#f0f9ff' : getScoreBgColor(kr.score),
                    color: getScoreColor(kr.score)
                  }"
                  @mouseenter="scoreHoverVisible[index] = true"
                  @mouseleave="scoreHoverVisible[index] = false"
                  @click="editScore(index)"
                >
                  {{ editScoreVisible[index] ? '' : formatScore(kr.score) }}
                  <input 
                    v-if="editScoreVisible[index]"
                    v-model.number="kr.score"
                    type="number"
                    min="0"
                    max="5"
                    step="0.1"
                    @blur="saveScore(index)"
                    @keyup.enter="saveScore(index)"
                    style="width: 35px; margin-left: 3px; padding: 1px 3px; border: 1px solid #409EFF; border-radius: 3px; font-size: 12px; text-align: center;"
                    autofocus
                  />
                </div>
              </div>
              <div style="display: flex; align-items: center;">
                <div class="delete-menu-container" style="position: relative;">
                  <el-icon 
                    style="font-size: 15px; color: #909399; cursor: pointer; transition: all 0.3s;"
                    @click="toggleDeleteMenu(index)"
                  >
                    <MoreFilled />
                  </el-icon>
                  <div v-if="deleteMenuVisible[index]" 
                       style="position: absolute; top: 100%; right: 0; margin-top: 3px; z-index: 1000; min-width: 100px; padding: 4px; background-color: #FFFFFF; border: 1px solid #E4E7ED; border-radius: 4px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);">
                    <div 
                      @click="deleteKeyResult(index)"
                      @mouseenter="isDeleteHovered = true"
                      @mouseleave="isDeleteHovered = false"
                      :style="{
                        padding: '6px 10px',
                        fontSize: '12px',
                        color: '#F56C6C',
                        cursor: 'pointer',
                        transition: 'all 0.2s',
                        borderRadius: '3px',
                        backgroundColor: isDeleteHovered ? '#FEF0F0' : '#FFFFFF'
                      }"
                    >
                      删除
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div v-if="!showAddKeyResult" 
             @click="showAddKeyResult = true"
             style="margin-bottom: 4px; padding: 5px; border: 2px dashed #E4E7ED; border-radius: 6px; background-color: #F5F7FA; cursor: pointer; text-align: center; transition: all 0.3s;">
          <div style="display: flex; align-items: center; justify-content: center; gap: 4px; color: #909399; font-size: 12px;">
            <span style="font-size: 15px; color: #409EFF;">+</span>
            <span>添加新的 Key Result</span>
          </div>
        </div>
        
        <div v-if="showAddKeyResult" 
             style="margin-bottom: 4px; padding: 5px; border: 1px solid #409EFF; border-radius: 6px; background-color: #FFFFFF; transition: all 0.3s; position: relative;">
          <div style="display: flex; justify-content: space-between; align-items: center; gap: 10px;">
            <div style="flex: 1;">
              <input 
                v-model="newKeyResult.title"
                type="text"
                placeholder="请输入 Key Result"
                style="width: 100%; padding: 3px 5px; border: 1px solid #E4E7ED; border-radius: 4px; font-size: 13px; font-weight: 500; color: #303133; outline: none; transition: all 0.3s;"
              />
            </div>
            <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
              <div style="display: flex; align-items: center; gap: 3px;">
                <span style="font-size: 11px; color: #909399;">进度</span>
                <input 
                  v-model.number="newKeyResult.progress"
                  type="number"
                  min="0"
                  max="100"
                  placeholder="0"
                  style="width: 40px; padding: 2px 3px; border: 1px solid #E4E7ED; border-radius: 3px; font-size: 12px; outline: none; transition: all 0.3s; text-align: center;"
                />
              </div>
              <div style="display: flex; align-items: center; gap: 3px;">
                <span style="font-size: 11px; color: #909399;">权重</span>
                <input 
                  v-model.number="newKeyResult.weight"
                  type="number"
                  min="0"
                  max="100"
                  placeholder="10"
                  style="width: 40px; padding: 2px 3px; border: 1px solid #E4E7ED; border-radius: 3px; font-size: 12px; outline: none; transition: all 0.3s; text-align: center;"
                />
              </div>
              <div style="display: flex; align-items: center; gap: 3px;">
                <span style="font-size: 11px; color: #909399;">评分</span>
                <input 
                  v-model.number="newKeyResult.score"
                  type="number"
                  min="0"
                  max="5"
                  step="0.1"
                  placeholder="3.0"
                  style="width: 40px; padding: 2px 3px; border: 1px solid #E4E7ED; border-radius: 3px; font-size: 12px; outline: none; transition: all 0.3s; text-align: center;"
                />
              </div>
              <div style="display: flex; gap: 4px;">
                <button 
                  @click="addKeyResult"
                  style="padding: 3px 6px; background-color: #409EFF; color: #FFFFFF; border: none; border-radius: 4px; font-size: 11px; font-weight: 500; cursor: pointer; transition: all 0.3s;"
                >
                  确认
                </button>
                <button 
                  @click="cancelAddKeyResult"
                  style="padding: 3px 6px; background-color: #FFFFFF; color: #606266; border: 1px solid #E4E7ED; border-radius: 4px; font-size: 11px; font-weight: 500; cursor: pointer; transition: all 0.3s;"
                >
                  取消
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>



      <div style="margin-top: 12px; padding-top: 10px; border-top: 1px solid #E4E7ED;">
        <h4 style="margin: 0 0 10px 0; font-size: 13px; font-weight: 600; color: #303133;">评论</h4>
        
        <div v-if="comments.length > 0" style="margin-bottom: 12px;">
          <div v-for="(comment, index) in comments" :key="comment.id" style="margin-bottom: 10px; padding: 6px; background-color: #F5F7FA; border-radius: 4px;">
            <div style="display: flex; align-items: center; justify-content: space-between; gap: 6px; margin-bottom: 4px;">
              <div style="display: flex; align-items: center; gap: 6px;">
                <el-avatar :size="20" :src="comment.avatar" />
                <div>
                  <div style="font-size: 12px; font-weight: 500; color: #303133;">{{ comment.author }}</div>
                  <div style="font-size: 10px; color: #909399;">{{ comment.time }}</div>
                </div>
              </div>
              <button
                @click="deleteComment(index)"
                style="font-size: 10px; color: #F56C6C; background: none; border: none; cursor: pointer; padding: 2px 4px; border-radius: 3px; transition: all 0.2s;"
                :style="{ backgroundColor: 'transparent', border: 'none' }"
              >
                删除
              </button>
            </div>
            <div style="font-size: 12px; color: #606266; line-height: 1.4; padding-left: 26px;">
              {{ comment.content }}
            </div>
          </div>
        </div>
        
        <div style="display: flex; gap: 6px; align-items: flex-start;">
          <el-avatar :size="24" :src="currentUserAvatar" />
          <div style="flex: 1;">
            <textarea
              v-model="newComment"
              placeholder="写下你的评论..."
              style="width: 100%; padding: 6px; border: 1px solid #E4E7ED; border-radius: 4px; font-size: 12px; outline: none; transition: all 0.3s; resize: vertical; min-height: 50px; font-family: inherit;"
            />
            <div style="margin-top: 4px; display: flex; justify-content: flex-end;">
              <button
                @click="addComment"
                :disabled="!newComment.trim()"
                :style="{
                  padding: '3px 10px',
                  backgroundColor: newComment.trim() ? '#409EFF' : '#C0C4CC',
                  color: '#FFFFFF',
                  border: 'none',
                  borderRadius: '3px',
                  fontSize: '12px',
                  fontWeight: '500',
                  cursor: newComment.trim() ? 'pointer' : 'not-allowed',
                  transition: 'all 0.3s'
                }"
              >
                发送
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </el-card>
  
  <el-dialog
    v-model="showAllParticipants"
    title="所有参与人员"
    width="600px"
    :close-on-click-modal="true"
  >
    <div style="max-height: 400px; overflow-y: auto;">
      <div v-for="participant in props.participants" :key="participant.id" style="margin-bottom: 16px; padding: 12px; background-color: #F5F7FA; border-radius: 8px;">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
          <el-avatar :size="40" :src="participant.avatar" />
          <div style="flex: 1;">
            <div style="font-size: 14px; font-weight: 600; color: #303133;">{{ participant.name }}</div>
            <div style="font-size: 12px; color: #909399;">{{ participant.role }}</div>
            <div style="font-size: 11px; color: #409EFF; margin-top: 4px;">
              总进度: {{ getParticipantTotalProgress(participant.tasks || []) }}%
            </div>
          </div>
        </div>
        <div style="font-size: 12px; line-height: 1.5;">
          <div style="margin-bottom: 6px; color: #606266; font-weight: 500;">负责任务:</div>
          <div v-if="getParticipantTasks(participant.id).length > 0" style="line-height: 1.6;">
            <div v-for="task in getParticipantTasks(participant.id)" :key="task.id" style="margin-bottom: 8px; padding: 8px; background-color: #FFFFFF; border-radius: 6px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <span style="font-size: 11px; font-weight: 500; color: #303133;">{{ task.title }}</span>
                <span style="font-size: 10px; color: #67C23A; font-weight: 600;">{{ task.progress }}%</span>
              </div>
              <div style="margin-top: 4px; padding-left: 12px;">
                <div v-for="subtask in task.subtasks" :key="subtask.id" style="font-size: 10px; color: #909399; margin-bottom: 2px; display: flex; justify-content: space-between;">
                  <span>{{ subtask.title }}</span>
                  <span style="color: #606266;">{{ subtask.progress }}%</span>
                </div>
              </div>
            </div>
          </div>
          <div v-else style="color: #909399; font-size: 11px;">暂无具体任务</div>
        </div>
      </div>
    </div>
  </el-dialog>
</template>

<style scoped>
input[type=number]::-webkit-inner-spin-button, 
input[type=number]::-webkit-outer-spin-button { 
  -webkit-appearance: none; 
  margin: 0; 
}
</style>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue';
import { MoreFilled } from '@element-plus/icons-vue';
import { ElMessageBox, ElMessage, ElTooltip } from 'element-plus';

interface CardSubTask {
  id: number;
  title: string;
  progress: number;
}

interface CardTask {
  id: number;
  title: string;
  progress: number;
  subtasks: CardSubTask[];
}

interface CardParticipant {
  id: number;
  name: string;
  avatar: string;
  role: string;
  tasks?: CardTask[];
}

interface KeyResult {
  id: number;
  title: string;
  progress: number;
  weight: number;
  score: number;
  status: 'normal' | 'risk' | 'delayed';
}

interface Comment {
  id: number;
  author: string;
  avatar: string;
  content: string;
  time: string;
}

interface OkrCardProps {
  objective: string;
  owner: string;
  ownerId: number;
  participants: CardParticipant[];
  keyResults: KeyResult[];
  totalScore: number;
  createdDate?: string;
  isFollowed: (memberId: number) => boolean;
  toggleFollow: (memberId: number, memberName: string) => void;
}

const props = defineProps<OkrCardProps>();
const emit = defineEmits<{
  'select-participant': [participant: CardParticipant];
}>();


const hoveredParticipant = ref<CardParticipant | null>(null);
const hideTimer = ref<number | null>(null);
const showAddKeyResult = ref(false);
const deleteMenuVisible = ref<boolean[]>([]);
const isDeleteHovered = ref(false);
const localKeyResults = ref<KeyResult[]>([...(props.keyResults || [])]);
const showAllParticipants = ref(false);
const comments = ref<Comment[]>([]);
const newComment = ref('');
const currentUserAvatar = computed(() => {
  return 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png';
});
const currentUserName = computed(() => {
  return '当前用户';
});
const localTotalScore = ref<number>(props.totalScore);
const scoreHoverVisible = ref<boolean[]>([]);
const editScoreVisible = ref<boolean[]>([]);
const editTotalScore = ref<boolean>(false);
const progressHoverVisible = ref<boolean[]>([]);
const progressDialogVisible = ref<boolean[]>([]);
const currentEditingProgressIndex = ref<number>(-1);
const tempProgress = ref<number>(0);
const tempStatus = ref<'normal' | 'risk' | 'delayed'>('normal');
const weightError = ref(false);
const originalWeights = ref<number[]>([]);
const currentEditingIndex = ref<number>(-1);
const weightHoveredIndex = ref<number>(-1);
const fixedWeightHovered = ref(false);
const newKeyResult = ref({
  title: '',
  progress: 0,
  weight: 10,
  score: 3.0,
  status: 'normal' as 'normal' | 'risk' | 'delayed'
});

const visibleParticipants = computed(() => {
  const maxVisible = 4;
  if (props.participants.length <= maxVisible) {
    return props.participants;
  }
  return props.participants.slice(0, maxVisible);
});

const hiddenParticipants = computed(() => {
  const maxVisible = 4;
  if (props.participants.length <= maxVisible) {
    return [];
  }
  return props.participants.slice(maxVisible);
});

const totalProgress = computed(() => {
  if (!localKeyResults.value || localKeyResults.value.length === 0) return 0;
  const weightedSum = localKeyResults.value.reduce((sum, kr) => sum + (kr.progress * kr.weight), 0);
  return Math.round(weightedSum / 100);
});

onMounted(() => {
  deleteMenuVisible.value = new Array(localKeyResults.value.length).fill(false);
  scoreHoverVisible.value = new Array(localKeyResults.value.length).fill(false);
  editScoreVisible.value = new Array(localKeyResults.value.length).fill(false);
  progressHoverVisible.value = new Array(localKeyResults.value.length).fill(false);
  
  localKeyResults.value.forEach((kr, index) => {
    if (kr.status === undefined || kr.status === null || kr.status === '') {
      kr.status = 'normal';
    }
  });
  
  // 初始化用户信息
  
  
  document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
});

const handleClickOutside = (event: MouseEvent) => {
  const target = event.target as HTMLElement;
  if (!target.closest('.delete-menu-container')) {
    deleteMenuVisible.value = deleteMenuVisible.value.map(() => false);
  }
};

const showParticipantInfo = (participant: CardParticipant) => {
  cancelHideTimer();
  hoveredParticipant.value = participant;
};

const startHideTimer = () => {
  hideTimer.value = window.setTimeout(() => {
    hoveredParticipant.value = null;
  }, 200);
};

const cancelHideTimer = () => {
  if (hideTimer.value !== null) {
    clearTimeout(hideTimer.value);
    hideTimer.value = null;
  }
};

const getParticipantTasks = (participantId: number): CardTask[] => {
  const participant = props.participants.find(p => p.id === participantId);
  if (participant && participant.tasks) {
    return participant.tasks;
  }
  return [];
};

const getParticipantTotalProgress = (tasks: CardTask[]): number => {
  if (!tasks || tasks.length === 0) return 0;
  const totalProgress = tasks.reduce((sum, task) => sum + task.progress, 0);
  return Math.round(totalProgress / tasks.length);
};

const getProgressColor = (progress: number): string => {
  if (progress >= 80) return '#67C23A';
  if (progress >= 50) return '#E6A23C';
  return '#F56C6C';
};

const getProgressColorByStatus = (status: 'normal' | 'risk' | 'delayed'): string => {
  if (status === 'normal') return '#67C23A';
  if (status === 'risk') return '#F56C6C';
  return '#9C27B0';
};

const getProgressTextColor = (status: 'normal' | 'risk' | 'delayed'): string => {
  if (status === 'normal') return '#67C23A';
  if (status === 'risk') return '#F56C6C';
  return '#9C27B0';
};



const addKeyResult = () => {
  if (newKeyResult.value.title.trim() !== '') {
    const newWeight = newKeyResult.value.weight;
    
    // 计算当前总权重
    const currentTotalWeight = localKeyResults.value.reduce((sum, kr) => sum + kr.weight, 0);
    // 计算需要调整的权重值
    const adjustmentNeeded = 100 - (currentTotalWeight + newWeight);
    
    // 生成确认消息
    let confirmMessage = `添加新的 Key Result 后，系统将自动调整现有任务的权重以确保总和为 100%。`;
    if (adjustmentNeeded > 0) {
      confirmMessage += `\n\n需要增加现有任务的权重总计 ${adjustmentNeeded}%。`;
    } else if (adjustmentNeeded < 0) {
      confirmMessage += `\n\n需要减少现有任务的权重总计 ${Math.abs(adjustmentNeeded)}%。`;
    }
    confirmMessage += `\n\n确定要添加吗？`;
    
    // 显示确认对话框
    ElMessageBox.confirm(
      confirmMessage,
      '确认添加 Key Result',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'info',
      }
    ).then(() => {
      const id = localKeyResults.value.length > 0 ? Math.max(...localKeyResults.value.map(kr => kr.id)) + 1 : 1;
      
      // 添加新的 Key Result
      localKeyResults.value.push({
        id,
        title: newKeyResult.value.title,
        progress: newKeyResult.value.progress,
        weight: newWeight,
        score: newKeyResult.value.score,
        status: 'normal'
      });
      
      // 调整现有 Key Result 的权重，确保总和为 100%
      if (adjustmentNeeded !== 0 && localKeyResults.value.length > 1) {
        // 取最后一个 Key Result（新添加的）
        const keyResults = localKeyResults.value as KeyResult[];
        const lastIndex = keyResults.length - 1;
        let remainingAdjustment = adjustmentNeeded;
        
        // 从第一个 Key Result 开始调整
        for (let i = 0; i < lastIndex; i++) {
          const currentKr = keyResults[i] as KeyResult;
          if (currentKr) {
            if (remainingAdjustment > 0) {
              // 如果需要增加权重，从第一个开始增加
              const maxPossibleIncrease = Math.min(remainingAdjustment, 100 - currentKr.weight);
              currentKr.weight += maxPossibleIncrease;
              remainingAdjustment -= maxPossibleIncrease;
            } else {
              // 如果需要减少权重，从第一个开始减少
              const maxPossibleDecrease = Math.min(Math.abs(remainingAdjustment), currentKr.weight);
              currentKr.weight -= maxPossibleDecrease;
              remainingAdjustment += maxPossibleDecrease;
            }
          }
          
          if (remainingAdjustment === 0) break;
        }
        
        // 最后一个 Key Result 作为调整项，确保总和为 100%
        const adjustedTotal = keyResults.slice(0, lastIndex).reduce((sum, kr) => {
          return kr ? sum + kr.weight : sum;
        }, 0);
        if (keyResults[lastIndex]) {
          keyResults[lastIndex].weight = 100 - adjustedTotal;
        }
      }
      
      newKeyResult.value = {
        title: '',
        progress: 0,
        weight: 10,
        score: 3.0
      };
      showAddKeyResult.value = false;
      ElMessage.success('Key Result 添加成功，权重已自动调整');
    }).catch(() => {
      ElMessage.info('已取消添加');
    });
  }
};

const toggleDeleteMenu = (index: number) => {
  deleteMenuVisible.value[index] = !deleteMenuVisible.value[index];
};

const deleteKeyResult = (index: number) => {
  ElMessageBox.confirm(
    '你确定要删除这项keyresult吗？',
    '确认删除',
    {
      confirmButtonText: '确认',
      cancelButtonText: '取消',
      type: 'warning',
    }
  ).then(() => {
    localKeyResults.value.splice(index, 1);
    deleteMenuVisible.value.splice(index, 1);
    ElMessage.success('删除成功');
  }).catch(() => {
    ElMessage.info('已取消删除');
  });
};

const deleteComment = (index: number) => {
  ElMessageBox.confirm(
    '你确定要删除这条评论吗？',
    '确认删除',
    {
      confirmButtonText: '确认',
      cancelButtonText: '取消',
      type: 'warning',
    }
  ).then(() => {
    comments.value.splice(index, 1);
    ElMessage.success('删除成功');
  }).catch(() => {
    ElMessage.info('已取消删除');
  });
};

const adjustWeights = (changedIndex: number) => {
  // 确保数组存在且索引有效
  if (!localKeyResults.value || localKeyResults.value.length === 0 || changedIndex < 0 || changedIndex >= localKeyResults.value.length) {
    return;
  }
  
  // 设置当前正在编辑的索引
  currentEditingIndex.value = changedIndex;
  
  // 确保权重不为负数且为整数
  let newWeight = localKeyResults.value[changedIndex].weight;
  if (newWeight < 0) {
    newWeight = 0;
  }
  newWeight = Math.round(newWeight);
  
  // 只有当有多个Key Result时才需要调整
  if (localKeyResults.value.length > 1) {
    // 计算除最后一项外的总权重
    const lastIndex = localKeyResults.value.length - 1;
    let sumWithoutLast = 0;
    
    // 计算除最后一项外的总权重（使用新的权重值）
    for (let i = 0; i < localKeyResults.value.length; i++) {
      if (i === changedIndex) {
        sumWithoutLast += newWeight;
      } else if (i !== lastIndex) {
        sumWithoutLast += localKeyResults.value[i].weight;
      }
    }
    
    // 计算最后一项的权重，确保总和为 100%
    const lastWeight = 100 - sumWithoutLast;
    
    // 检查最后一项权重是否为非正数
    if (lastWeight <= 0) {
      // 显示错误信息
      weightError.value = true;
      // 重置输入框的值为原始值
      localKeyResults.value[changedIndex].weight = originalWeights.value[changedIndex];
    } else {
      // 隐藏错误信息
      weightError.value = false;
      // 更新权重值
      localKeyResults.value[changedIndex].weight = newWeight;
      localKeyResults.value[lastIndex].weight = lastWeight;
    }
  } else {
    // 只有一项时，确保其权重为100%
    localKeyResults.value[0].weight = 100;
    weightError.value = false;
  }
};

const onWeightInput = (index: number, event: Event) => {
  // 保存原始权重值，用于回滚
  originalWeights.value = localKeyResults.value.map(kr => kr.weight);
  
  const target = event.target as HTMLInputElement;
  const value = parseInt(target.value) || 0;
  localKeyResults.value[index].weight = value;
  adjustWeights(index);
};

const editScore = (index: number) => {
  editScoreVisible.value[index] = true;
};

const saveScore = (index: number) => {
  editScoreVisible.value[index] = false;
};

const openProgressDialog = (index: number) => {
  currentEditingProgressIndex.value = index;
  tempProgress.value = localKeyResults.value[index].progress;
  tempStatus.value = localKeyResults.value[index].status || 'normal';
  // 确保数组长度足够
  while (progressDialogVisible.value.length <= index) {
    progressDialogVisible.value.push(false);
  }
  // 关闭所有其他弹窗
  progressDialogVisible.value.forEach((_, i) => {
    progressDialogVisible.value[i] = false;
  });
  // 打开当前索引的弹窗
  progressDialogVisible.value[index] = true;
};

const saveProgress = () => {
  if (currentEditingProgressIndex.value >= 0 && currentEditingProgressIndex.value < localKeyResults.value.length) {
    localKeyResults.value[currentEditingProgressIndex.value].progress = tempProgress.value;
    localKeyResults.value[currentEditingProgressIndex.value].status = tempStatus.value;
  }
  // 关闭对应索引的弹窗
  if (currentEditingProgressIndex.value >= 0) {
    progressDialogVisible.value[currentEditingProgressIndex.value] = false;
  }
};

// 点击其他地方关闭弹窗
const closeProgressDialogOnClickOutside = (event: MouseEvent) => {
  // 检查点击是否在弹窗或进度板块内
  const target = event.target as HTMLElement;
  const isClickInsideDialog = target.closest('[data-progress-dialog]');
  const isClickInsideProgressSection = target.closest('[data-progress-section]');
  
  if (!isClickInsideDialog && !isClickInsideProgressSection) {
    // 关闭所有弹窗
    progressDialogVisible.value.forEach((_, index) => {
      progressDialogVisible.value[index] = false;
    });
  }
};

// 组件挂载时添加全局点击事件监听器
onMounted(() => {
  document.addEventListener('click', closeProgressDialogOnClickOutside);
});

// 组件卸载时移除全局点击事件监听器
onUnmounted(() => {
  document.removeEventListener('click', closeProgressDialogOnClickOutside);
});

const getScoreBgColor = (score: number): string => {
  if (score >= 4.0) return '#f0f9eb';
  if (score >= 3.0) return '#ecf5ff';
  if (score >= 2.0) return '#fdf6ec';
  return '#fef0f0';
};

const getScoreColor = (score: number): string => {
  if (score >= 4.0) return '#67C23A';
  if (score >= 3.0) return '#409EFF';
  if (score >= 2.0) return '#E6A23C';
  return '#F56C6C';
};

const formatScore = (score: number): string => {
  return score.toFixed(1);
};

// 回滚权重到修改前的值
const rollbackWeights = () => {
  if (originalWeights.value.length > 0 && localKeyResults.value.length > 0) {
    localKeyResults.value.forEach((kr, index) => {
      if (index < originalWeights.value.length) {
        kr.weight = originalWeights.value[index];
      }
    });
    weightError.value = false;
  }
};

// 检查权重是否有效
const isWeightValid = () => {
  if (localKeyResults.value.length <= 1) {
    return true;
  }
  
  const lastIndex = localKeyResults.value.length - 1;
  return localKeyResults.value[lastIndex].weight > 0;
};

const cancelAddKeyResult = () => {
  newKeyResult.value = {
    title: '',
    progress: 0,
    weight: 10,
    score: 3.0
  };
  showAddKeyResult.value = false;
};

const addComment = () => {
  if (newComment.value.trim() !== '') {
    const now = new Date();
    const time = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')} ${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}`;
    
    comments.value.push({
      id: Date.now(),
      author: currentUserName.value,
      avatar: currentUserAvatar.value,
      content: newComment.value.trim(),
      time
    });
    newComment.value = '';
    ElMessage.success('评论发表成功');
  }
};
</script>
