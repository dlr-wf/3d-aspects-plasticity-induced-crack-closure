# imports

import matplotlib.pyplot as plt
import pandas as pd

Params = {'backend': 'ps',
          'text.usetex': False}
plt.rcParams.update(Params)

FigParams = {'figure.figsize': [10, 6],
             'figure.autolayout': True,
             'figure.dpi': 300,
             'figure.frameon': True,
             'figure.facecolor': 'white',
             'figure.edgecolor': 'white'}
plt.rcParams.update(FigParams)

LegendParams = {'legend.loc': 'upper left',
                'legend.frameon': True,
                'legend.framealpha': 1,
                'legend.facecolor': 'inherit',
                'legend.edgecolor': 'black',
                'legend.fancybox': False,
                'legend.shadow': False,
                'legend.markerscale': 1,
                'legend.fontsize': 24,
                'legend.title_fontsize': 24,
                'legend.labelspacing': 0.5,
                'legend.columnspacing': 2.0}
plt.rcParams.update(LegendParams)

AxesParams = {'axes.facecolor': 'white',
              'axes.edgecolor': 'black',
              'axes.linewidth': 1.5,
              'axes.grid': True,
              'axes.grid.axis': 'both',
              'axes.labelsize': 24,
              'axes.labelpad': 4.0,
              'axes.formatter.limits': [-2, 3],
              'axes.formatter.use_locale': False,
              'axes.formatter.use_mathtext': False,
              'axes.formatter.useoffset': True,
              'axes.formatter.offset_threshold': 4,
              'axes.spines.left': True,
              'axes.spines.bottom': True,
              'axes.spines.right': True,
              'axes.spines.top': True,
              'axes.autolimit_mode': 'data'}  # 'data' or 'round_numbers'
plt.rcParams.update(AxesParams)

TicksParams = {'xtick.bottom': True,
               'xtick.top': True,
               'ytick.left': True,
               'ytick.right': True,
               'xtick.direction': 'in',
               'ytick.direction': 'in',
               'xtick.minor.visible': True,
               'ytick.minor.visible': True,
               'xtick.major.size': 12,
               'xtick.minor.size': 6,
               'xtick.major.width': 1.5,
               'xtick.minor.width': 1.5,
               'xtick.major.pad': 12,
               'xtick.minor.pad': 4,
               'ytick.major.size': 12,
               'ytick.minor.size': 6,
               'ytick.major.width': 1.5,
               'ytick.minor.width': 1.5,
               'ytick.major.pad': 12,
               'ytick.minor.pad': 4,
               'xtick.labelsize': 24,
               'ytick.labelsize': 24}
plt.rcParams.update(TicksParams)

GridParams = {'grid.color': 'b0b0b0',
              'grid.linestyle': '--',
              'grid.linewidth': 0.9,
              'grid.alpha': 1}
plt.rcParams.update(GridParams)

LineParams = {'lines.linewidth': 3,
              'lines.linestyle': '-',
              'lines.marker': None,
              'lines.markerfacecolor': 'auto',
              'lines.markeredgecolor': 'auto',
              'lines.markersize': 16}
plt.rcParams.update(LineParams)


def importdata(path_data):
    # import data
    lnames = []
    dRowData = pd.read_csv(path_data, sep=',', header=None)
    for iColumn in range(0, len(dRowData.columns)):
        temp = dRowData.iloc[0, iColumn]
        lnames.append(temp.strip())
    data = pd.read_csv(path_data, sep=',', header=0, names=lnames)
    return data


plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111)
data = pd.read_excel('Rkonst.xlsx', sheet_name='Pres')
ax.plot(data['t'], data['k15'], marker='x', label='15')
ax.plot(data['t'], data['k20'], marker='x', label='20')
ax.plot(data['t'], data['k25'], marker='x', label='25')
ax.plot(data['t'], data['k30'], marker='x', label='30')
ax.plot(data['t'], data['k35'], marker='x', label='35')
ax.set_xlim(0.5, 10.5)
ax.set_xlabel('sheet thickness $t$ [mm]')
ax.set_ylabel('contact pressure $p_{\\mathrm{c}}$ [MPa]')
ax.set_title('constant $R$=0.0', fontsize=24)
ax.legend(bbox_to_anchor=(1.04, 1.0), loc='upper left', title='$K_{I,max}$\n[MPa√m]')._legend_box.align = 'left'
savefile = 'r_konst_pres.png'
plt.savefig(savefile, dpi=300)

plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111)
data = pd.read_excel('Rkonst.xlsx', sheet_name='A')
ax.plot(data['t'], data['k15'], marker='x', label='15')
ax.plot(data['t'], data['k20'], marker='x', label='20')
ax.plot(data['t'], data['k25'], marker='x', label='25')
ax.plot(data['t'], data['k30'], marker='x', label='30')
ax.plot(data['t'], data['k35'], marker='x', label='35')
ax.set_xlim(0.5, 10.5)
ax.set_xlabel('sheet thickness $t$ [mm]')
ax.set_ylabel('realtive contact area $A_c$ [1]')
ax.set_title('constant $R$=0.0', fontsize=24)
ax.legend(bbox_to_anchor=(1.04, 1.0), loc='upper left', title='$K_{I,max}$\n[MPa√m]')._legend_box.align = 'left'
savefile = 'r_konst_A.png'
plt.savefig(savefile, dpi=300)

plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111)
data = pd.read_excel('Kkonst.xlsx', sheet_name='pres')
ax.plot(data['R'], data['t1'], marker='x', label='1')
ax.plot(data['R'], data['t2'], marker='x', label='2')
ax.plot(data['R'], data['t3'], marker='x', label='3')
ax.plot(data['R'], data['t4'], marker='x', label='4')
ax.plot(data['R'], data['t5'], marker='x', label='5')
ax.plot(data['R'], data['t6'], marker='x', label='6')
ax.plot(data['R'], data['t7'], marker='x', label='7')
ax.plot(data['R'], data['t8'], marker='x', label='8')
ax.plot(data['R'], data['t9'], marker='x', label='9')
ax.plot(data['R'], data['t10'], marker='x', label='10')
ax.set_xlabel('load ratio $R$ [1]')
ax.set_ylabel('contact pressure $p_{\\mathrm{c}}$ [MPa]')
ax.set_title('constant $K_{I,max}$=20 MPa√m', fontsize=24)
ax.legend(bbox_to_anchor=(1.04, 1.1), loc='upper left', title='$t$ [mm]')._legend_box.align = 'left'
savefile = 'k_konst_pres.png'
plt.savefig(savefile, dpi=300)

plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111)
data = pd.read_excel('Kkonst.xlsx', sheet_name='a')
ax.plot(data['R'], data['t1'], marker='x', label='1')
ax.plot(data['R'], data['t2'], marker='x', label='2')
ax.plot(data['R'], data['t3'], marker='x', label='3')
ax.plot(data['R'], data['t4'], marker='x', label='4')
ax.plot(data['R'], data['t5'], marker='x', label='5')
ax.plot(data['R'], data['t6'], marker='x', label='6')
ax.plot(data['R'], data['t7'], marker='x', label='7')
ax.plot(data['R'], data['t8'], marker='x', label='8')
ax.plot(data['R'], data['t9'], marker='x', label='9')
ax.plot(data['R'], data['t10'], marker='x', label='10')
ax.set_xlabel('load ratio $R$ [1]')
ax.set_ylabel('realtive contact area $A_{\\mathrm{c}}$ [1]')
ax.set_title('constant $K_{\\mathrm{I,max}}$=20 MPa√m', fontsize=24)
ax.legend(bbox_to_anchor=(1.04, 1.1), loc='upper left', title='$t$ [mm]')._legend_box.align = 'left'
savefile = 'k_konst_A.png'
plt.savefig(savefile, dpi=300)

plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111)
data = pd.read_excel('TKonst.xlsx', sheet_name='Pres')
ax.plot(data['K'], data['R0'], marker='x', label='0.0')
ax.plot(data['K'], data['R01'], marker='x', label='0.1')
ax.plot(data['K'], data['R02'], marker='x', label='0.2')
ax.plot(data['K'], data['R03'], marker='x', label='0.3')
ax.set_xlabel('stress intensity factor $K_{\\mathrm{I,max}}$ [MPa√m]')
ax.set_ylabel('contact pressure $p_{\\mathrm{c}}$ [MPa]')
ax.set_title('constant $t$=4 mm', fontsize=24)
ax.legend(bbox_to_anchor=(1.04, 1.0), loc='upper left', title='$R$ [1]')._legend_box.align = 'left'
savefile = 't_konst_pres.png'
plt.savefig(savefile, dpi=300)

plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111)
data = pd.read_excel('TKonst.xlsx', sheet_name='A')
ax.plot(data['K'], data['R0'], marker='x', label='0.0')
ax.plot(data['K'], data['R01'], marker='x', label='0.1')
ax.plot(data['K'], data['R02'], marker='x', label='0.2')
ax.plot(data['K'], data['R03'], marker='x', label='0.3')
ax.set_xlabel('stress intensity factor $K_{\\mathrm{I,max}}$ [MPa√m]')
ax.set_ylabel('realtive contact area $A_{mathrm{c}}$ [1]')
ax.set_title('constant $t$=4 mm', fontsize=24)
ax.legend(bbox_to_anchor=(1.04, 1.0), loc='upper left', title='$R$ [1]')._legend_box.align = 'left'
savefile = 't_konst_A.png'
plt.savefig(savefile, dpi=300)
