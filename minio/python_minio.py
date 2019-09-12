import os
import time
from minio import Minio
from minio.select_object_options import SelectObjectOptions, InputSerialization, OutputSerialization,\
    CSVInput, CSVOutput, RequestProgress

file_path = '/home/yan/workspace/sample/regression/wiki_google.csv'
file_stat = os.stat(file_path)

c = Minio('127.0.0.1:9000', access_key='123456', secret_key='12345678', secure=False)


# with open(file_path, 'rb') as f:
#     c.put_object('test', 'google.csv', f, file_stat.st_size, content_type='application/csv')

options = SelectObjectOptions(
    expression='select * from s3object limit 100 ',
    input_serialization=InputSerialization(
        compression_type='NONE',
        csv=CSVInput(
            FileHeaderInfo='USE',
            RecordDelimiter='\n',
            FieldDelimiter=',',
            QuoteCharacter='"',
            QuoteEscapeCharacter='"',
            Comments='#',
            AllowQuotedRecordDelimiter='False'
        )
    ),
    output_serialization=OutputSerialization(
        csv=CSVOutput(
            QuoteFields='ASNEEDED',
            RecordDelimiter='\n',
            FieldDelimiter=',',
            QuoteCharacter='"',
            QuoteEscapeCharacter='"'
        )
    ),
    request_progress=RequestProgress(
        enabled='False'
    )
)

start = time.time()
data = c.select_object_content('test', 'springleaf.csv', options)
with open('springleaf_1.csv', 'w') as f:
    for d in data.stream(10 * 1024):
        f.write(d)
print(time.time()-start)


