if True:
    import sys

    sys.path.append('../../../')
    import dash
    import feffery_antd_components as fac

app = dash.Dash(__name__)

app.layout = dash.html.Div(
    [
        fac.AntdTable(
            data=[
                {
                    'parent_id': 0,
                    'subject_id': 5,
                    'subjectName': '1费用',
                    '2024-01': 129070.69,
                    '2024-02': 6920.25,
                    '2024-03': 8692.08,
                    '2024-04': 11505.06,
                    '2024-05': 6020.31,
                    '合计': 162208.39,
                    '占比': '37.86%',
                    'children': [
                        {
                            'parent_id': 5,
                            'subject_id': 43,
                            'subjectName': '2付款',
                            '2024-01': 126307.66,
                            '2024-02': 3664.12,
                            '2024-03': 1941.0,
                            '2024-04': 7465.98,
                            '2024-05': 3820.8,
                            '合计': 143199.56,
                            '占比': '33.42%',
                        },
                        {
                            'parent_id': 5,
                            'subject_id': 84,
                            'subjectName': '3旅费',
                            '2024-01': 0.0,
                            '2024-02': 0.0,
                            '2024-03': 5878.31,
                            '2024-04': 3834.84,
                            '2024-05': 0.0,
                            '合计': 9713.15,
                            '占比': '2.27%',
                        },
                        {
                            'parent_id': 5,
                            'subject_id': 38,
                            'subjectName': '4金',
                            '2024-01': 2763.03,
                            '2024-02': 3256.13,
                            '2024-03': 872.77,
                            '2024-04': 204.24,
                            '2024-05': 2199.51,
                            '合计': 9295.68,
                            '占比': '2.17%',
                        },
                    ],
                },
                {
                    'parent_id': 0,
                    'subject_id': 96,
                    'subjectName': '1酬',
                    '2024-01': 43387.05,
                    '2024-02': 3757.05,
                    '2024-03': 4919.05,
                    '2024-04': 33102.51,
                    '2024-05': 9132.51,
                    '合计': 94298.17,
                    '占比': '22.01%',
                    'children': [
                        {
                            'parent_id': 96,
                            'subject_id': 75,
                            'subjectName': '2资',
                            '2024-01': 29000.0,
                            '2024-02': 0.0,
                            '2024-03': 0.0,
                            '2024-04': 24000.0,
                            '2024-05': 0.0,
                            '合计': 53000.0,
                            '占比': '12.37%',
                        },
                        {
                            'parent_id': 96,
                            'subject_id': 37,
                            'subjectName': '3资',
                            '2024-01': 10600.0,
                            '2024-02': 0.0,
                            '2024-03': 1162.0,
                            '2024-04': 5300.0,
                            '2024-05': 5300.0,
                            '合计': 22362.0,
                            '占比': '5.22%',
                        },
                        {
                            'parent_id': 96,
                            'subject_id': 71,
                            'subjectName': '2保',
                            '2024-01': 3757.05,
                            '2024-02': 3757.05,
                            '2024-03': 3757.05,
                            '2024-04': 3802.51,
                            '2024-05': 3802.51,
                            '合计': 18876.17,
                            '占比': '4.41%',
                        },
                        {
                            'parent_id': 96,
                            'subject_id': 63,
                            'subjectName': '4费',
                            '2024-01': 30.0,
                            '2024-02': 0.0,
                            '2024-03': 0.0,
                            '2024-04': 0.0,
                            '2024-05': 30.0,
                            '合计': 60.0,
                            '占比': '0.01%',
                        },
                    ],
                },
                {
                    'parent_id': 0,
                    'subject_id': 4,
                    'subjectName': '1费用',
                    '2024-01': 17608.0,
                    '2024-02': 17640.0,
                    '2024-03': 17528.0,
                    '2024-04': 17608.0,
                    '2024-05': 17629.0,
                    '合计': 88013.0,
                    '占比': '20.54%',
                    'children': [
                        {
                            'parent_id': 4,
                            'subject_id': 78,
                            'subjectName': '2金',
                            '2024-01': 17608.0,
                            '2024-02': 17640.0,
                            '2024-03': 17528.0,
                            '2024-04': 17608.0,
                            '2024-05': 17629.0,
                            '合计': 88013.0,
                            '占比': '20.54%',
                        }
                    ],
                },
                {
                    'parent_id': 0,
                    'subject_id': 6,
                    'subjectName': '3用',
                    '2024-01': 45773.61,
                    '2024-02': 145.0,
                    '2024-03': 22357.04,
                    '2024-04': 42.05,
                    '2024-05': 3397.9,
                    '合计': 71715.6,
                    '占比': '16.74%',
                    'children': [
                        {
                            'parent_id': 6,
                            'subject_id': 85,
                            'subjectName': '4出',
                            '2024-01': 44600.0,
                            '2024-02': 0.0,
                            '2024-03': 21600.0,
                            '2024-04': 0.0,
                            '2024-05': 0.0,
                            '合计': 66200.0,
                            '占比': '15.45%',
                        },
                        {
                            'parent_id': 6,
                            'subject_id': 61,
                            'subjectName': '2费',
                            '2024-01': 1173.61,
                            '2024-02': 145.0,
                            '2024-03': 757.04,
                            '2024-04': 42.05,
                            '2024-05': 3397.9,
                            '合计': 5515.6,
                            '占比': '1.29%',
                        },
                    ],
                },
                {
                    'parent_id': 0,
                    'subject_id': 8,
                    'subjectName': '2用',
                    '2024-01': 3779.09,
                    '2024-02': 212.61,
                    '2024-03': 1703.25,
                    '2024-04': 2190.72,
                    '2024-05': 2584.13,
                    '合计': 10469.8,
                    '占比': '2.44%',
                    'children': [
                        {
                            'parent_id': 8,
                            'subject_id': 58,
                            'subjectName': '3用',
                            '2024-01': 3523.09,
                            '2024-02': 173.61,
                            '2024-03': 1289.18,
                            '2024-04': 2000.84,
                            '2024-05': 2501.13,
                            '合计': 9487.85,
                            '占比': '2.21%',
                        },
                        {
                            'parent_id': 8,
                            'subject_id': 80,
                            'subjectName': '4车费',
                            '2024-01': 60.0,
                            '2024-02': 0.0,
                            '2024-03': 300.0,
                            '2024-04': 80.0,
                            '2024-05': 0.0,
                            '合计': 440.0,
                            '占比': '0.10%',
                        },
                        {
                            'parent_id': 8,
                            'subject_id': 57,
                            'subjectName': '5用',
                            '2024-01': 151.0,
                            '2024-02': 39.0,
                            '2024-03': 84.07,
                            '2024-04': 9.88,
                            '2024-05': 39.0,
                            '合计': 322.95,
                            '占比': '0.08%',
                        },
                        {
                            'parent_id': 8,
                            'subject_id': 73,
                            'subjectName': '1费',
                            '2024-01': 45.0,
                            '2024-02': 0.0,
                            '2024-03': 30.0,
                            '2024-04': 100.0,
                            '2024-05': 44.0,
                            '合计': 219.0,
                            '占比': '0.05%',
                        },
                    ],
                },
                {
                    'parent_id': 0,
                    'subject_id': 7,
                    'subjectName': '1用',
                    '2024-01': 80.0,
                    '2024-02': 0.0,
                    '2024-03': 543.25,
                    '2024-04': 410.0,
                    '2024-05': 402.49,
                    '合计': 1435.74,
                    '占比': '0.34%',
                    'children': [
                        {
                            'parent_id': 7,
                            'subject_id': 81,
                            'subjectName': '23',
                            '2024-01': 0.0,
                            '2024-02': 0.0,
                            '2024-03': 543.25,
                            '2024-04': 410.0,
                            '2024-05': 400.0,
                            '合计': 1353.25,
                            '占比': '0.32%',
                        },
                        {
                            'parent_id': 7,
                            'subject_id': 70,
                            'subjectName': '1费',
                            '2024-01': 80.0,
                            '2024-02': 0.0,
                            '2024-03': 0.0,
                            '2024-04': 0.0,
                            '2024-05': 2.49,
                            '合计': 82.49,
                            '占比': '0.02%',
                        },
                    ],
                },
                {
                    'parent_id': 0,
                    'subject_id': 3,
                    'subjectName': '4用',
                    '2024-01': 187.81,
                    '2024-02': 0.0,
                    '2024-03': 12.0,
                    '2024-04': 19.88,
                    '2024-05': 85.18,
                    '合计': 304.87,
                    '占比': '0.07%',
                    'children': [
                        {
                            'parent_id': 3,
                            'subject_id': 52,
                            'subjectName': '2入',
                            '2024-01': 186.38,
                            '2024-02': 0.0,
                            '2024-03': 0.0,
                            '2024-04': 0.0,
                            '2024-05': 0.0,
                            '合计': 186.38,
                            '占比': '0.04%',
                        },
                        {
                            'parent_id': 3,
                            'subject_id': 74,
                            'subjectName': '5费',
                            '2024-01': 1.43,
                            '2024-02': 0.0,
                            '2024-03': 12.0,
                            '2024-04': 19.88,
                            '2024-05': 85.18,
                            '合计': 118.49,
                            '占比': '0.03%',
                        },
                    ],
                },
            ],
            columns=[
                {
                    'title': '科目名称',
                    'dataIndex': 'subjectName',
                    'width': 150,
                    'fixed': 'left',
                },
                {
                    'title': '占比',
                    'dataIndex': '占比',
                    'width': 80,
                    'fixed': 'left',
                },
                {
                    'title': '合计',
                    'dataIndex': '合计',
                    'width': 100,
                    'fixed': 'left',
                },
                {
                    'title': '2024-01',
                    'dataIndex': '2024-01',
                    'width': 100,
                },
                {
                    'title': '2024-02',
                    'dataIndex': '2024-02',
                    'width': 100,
                },
                {
                    'title': '2024-03',
                    'dataIndex': '2024-03',
                    'width': 100,
                },
                {
                    'title': '2024-04',
                    'dataIndex': '2024-04',
                    'width': 100,
                },
                {
                    'title': '2024-05',
                    'dataIndex': '2024-05',
                    'width': 100,
                },
            ],
            **{
                'summaryRowContents': [
                    # 第一行
                    {
                        'content': fac.AntdText(''),
                        'align': 'center',
                    },
                    {
                        'content': fac.AntdText(''),
                        'align': 'center',
                    },
                    {
                        'content': fac.AntdText(''),
                        'align': 'center',
                    },
                    {
                        'content': fac.AntdText(
                            children='239886.25',
                            strong=True,
                        ),
                        'align': 'center',
                    },
                    {
                        'content': fac.AntdText(
                            children='28674.91', strong=True
                        ),
                        'align': 'center',
                    },
                    {
                        'content': fac.AntdText(
                            children='55754.67', strong=True
                        ),
                        'align': 'center',
                    },
                    {
                        'content': fac.AntdText(
                            children='64878.22', strong=True
                        ),
                        'align': 'center',
                    },
                    {
                        'content': fac.AntdText(
                            children='39251.52', strong=True
                        ),
                        'align': 'center',
                    },
                    {
                        'content': fac.AntdText(''),
                        'align': 'center',
                    },
                    {
                        'content': fac.AntdText(''),
                        'align': 'center',
                    },
                    {
                        'content': fac.AntdText(''),
                        'align': 'center',
                    },
                    {
                        'content': 324315.83,
                        'align': 'center',
                        'colSpan': 3,
                    },
                    {
                        'content': 104129.74,
                        'align': 'center',
                        'colSpan': 2,
                    },
                    {
                        'content': fac.AntdText(''),
                        'align': 'center',
                    },
                    {
                        'content': fac.AntdText(''),
                        'align': 'center',
                    },
                    {
                        'content': fac.AntdText(''),
                        'align': 'center',
                    },
                    {
                        'content': 428445.57,
                        'align': 'center',
                        'colSpan': 5,
                    },
                    {
                        'content': '支出合计： 428,445.57',
                        'align': 'center',
                        'colSpan': 8,
                    },
                ],
                'summaryRowBlankColumns': 1,
                'summaryRowFixed': 'bottom',
                'pagination': {'pageSize': 60},
                'rowSelectionType': 'radio',
            },
        )
    ]
)
if __name__ == '__main__':
    app.run(debug=True)
